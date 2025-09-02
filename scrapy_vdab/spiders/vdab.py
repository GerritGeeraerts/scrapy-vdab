import os
from datetime import datetime
import uuid
import requests


import scrapy
import json
from scrapy import signals

import scrapy_vdab.settings_dev

import scrapy_vdab.settings as settings
from scrapy_vdab.utils import (
    send_slack_notification, 
    dump_failure_data, 
    extract_request_data, 
    extract_response_data, 
    extract_error_data
)

class VdabSpider(scrapy.Spider):
    """
    Scrapy spider to scrape job listings from vdab.be.
    It searches for job postings based on predefined queries and criteria,
    then scrapes detailed information for each job.
    """
    name = 'vdab'
    allowed_domains = ['vdab.be']
    
    # URL for searching job listings
    search_url = 'https://www.vdab.be/rest/vindeenjob/v4/vacatureLight/zoek'
    
    # URL for retrieving detailed job information, formatted with job ID
    job_detail_url = 'https://www.vdab.be/rest/vindeenjob/v4/vacatures/{}?preview=false'

    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        """
        Initializes the spider with settings from the crawler.
        This method is used to set up paths for data storage, retrieve search queries
        and criteria, and configure Slack notifications.
        """
        spider = super().from_crawler(crawler, *args, **kwargs)

        # Generate current date components for directory structuring
        year = f"year={datetime.now().strftime('%Y')}"
        month = f"month={datetime.now().strftime('%m')}"
        day = f"day={datetime.now().strftime('%d')}"

        # Retrieve base and data lake directories from settings
        base_dir = crawler.settings.get('BASE_DIR')
        data_lake_dir = crawler.settings.get('DATA_LAKE_DIR')

        # Construct and create directory for storing job search results
        spider.job_search_path = os.path.join(base_dir, data_lake_dir, 'projects', 'jobs', 'bronze', 'vdab', 'job_searches', year, month, day)
        os.makedirs(spider.job_search_path, exist_ok=True)

        # Construct and create directory for storing individual job listing details
        spider.job_detail_path = os.path.join(base_dir, data_lake_dir, 'projects', 'jobs', 'bronze', 'vdab', 'job_listings', year, month, day)
        os.makedirs(spider.job_detail_path, exist_ok=True)
        
        # Construct and create directory for storing failure data
        spider.failure_path = os.path.join(base_dir, data_lake_dir, 'projects', 'jobs', 'bronze', 'vdab', 'failures', year, month, day)
        os.makedirs(spider.failure_path, exist_ok=True)

        # Retrieve search queries and criteria from settings
        spider.queries = crawler.settings.getlist('VDAB_SEARCH_QUERIES')
        spider.search_criteria = crawler.settings.getdict('VDAB_SEARCH_CRITERIA')

        # Configure Slack notifications based on settings
        spider.slack_enabled = crawler.settings.getbool('SLACK_NOTIFICATIONS_ENABLED')
        spider.slack_webhook_url = crawler.settings.get('SLACK_WEBHOOK_URL')
        spider.slack_max_notifications = crawler.settings.getint('SLACK_MAX_NOTIFICATIONS_PER_SPIDER', 10)

        # Connect the spider's error handler to the Scrapy spider_error signal
        crawler.signals.connect(spider.handle_error, signal=signals.spider_error)

        return spider


    def start_requests(self):
        """
        Initiates the scraping process by sending POST requests for each search query.
        Each request targets the `search_url` with specific criteria, including a keyword query.
        The `parse` method is set as the callback for processing the responses.
        """
        for query in self.queries:
            self.logger.info(f"Starting search for query: {query}")
            
            # Define the POST request body for job search
            post_data = {
                "criteria": {
                    "arbeidsduurCodes": [],
                    "arbeidsregimeCodes": [],
                    "attestCodes": [],
                    "beroepCodes": [],
                    "contractTypeCodes": [],
                    "diplomaCodes": [],
                    "ervaringCodes": [],
                    "internationaalCodes": [],
                    "jobdomeinCodes": [],
                    "rijbewijsCodes": [],
                    "taalCriteria": {
                        "taalSelecties": []
                    },
                    "trefwoord": query # The actual search keyword
                },
                "pagina": 1, # Start from the first page
                "paginaGrootte": 15, # Number of results per page
                "zoekmodus": "C2"
            }
            
            # Yield a POST request to the search URL
            yield scrapy.Request(
                url=self.search_url,
                method='POST',
                body=json.dumps(post_data),
                callback=self.parse,
                cb_kwargs={'post_data': post_data}, # Pass post_data for subsequent pagination
                errback=lambda failure: self.handle_error(failure, context="search_request")
            )

    def parse(self, response, post_data):
        """
        Parses the search results, saves them to a file, and extracts job IDs.
        For each job ID, it yields a request to fetch job details.
        If there are more pages of results, it yields a request for the next page.
        """
        query = post_data.get("criteria", {}).get("trefwoord")
        page = post_data.get("pagina")
        
        # Generate a unique filename for the search results
        filename = f"{query}-{page}-{uuid.uuid4()}.json"
        filepath = os.path.join(self.job_search_path, filename)
        
        # Save the raw search response body to a file
        with open(filepath, 'wb') as f:
            f.write(response.body)
        self.logger.info(f"Saved search results for query '{query}' page {page} to {filepath}")

        try:
            # Attempt to parse the response body as JSON
            data = response.json()
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to decode JSON from response: {response.url}")
            
            # Dump complete failure data
            error_data = {
                "type": "JSONDecodeError",
                "value": str(e),
                "traceback": None,
                "context": "search_response_parsing",
                "query": query,
                "page": page
            }
            
            failure_file = dump_failure_data(
                failure_path=self.failure_path,
                request_data=extract_request_data(response.request),
                response_data=extract_response_data(response),
                error_data=error_data,
                logger=self.logger
            )
            
            # Send Slack notification on JSON decoding failure
            message = (f"Spider '{self.name}' failed to decode JSON from search response: {response.url}\n"
                      f"Query: {query}, Page: {page}\n"
                      f"Failure data saved to: {failure_file}")
            send_slack_notification(self.logger, self.slack_enabled, self.slack_webhook_url, message, self.name, self.slack_max_notifications)
            return
        
        # Extract job results from the JSON data
        results = data.get('resultaten', [])
        self.logger.info(f"Found {len(results)} results for query '{query}' on page {page}")

        # Iterate through each job in the results and request its details
        for job in results:
            job_id = job.get('id', {}).get('id')
            if job_id:
                yield scrapy.Request(
                    url=self.job_detail_url.format(job_id),
                    callback=self.parse_job_details,
                    cb_kwargs={'job_id': job_id},
                    errback=lambda failure, jid=job_id: self.handle_error(failure, context=f"job_detail_request_{jid}")
                )
            else:
                self.logger.warning(f"Could not find job id in result: {job}")

        # If the number of results equals the page size, there might be more pages
        if len(results) == post_data['paginaGrootte']:
            post_data['pagina'] += 1 # Increment page number for the next request
            self.logger.info(f"Requesting next page ({post_data['pagina']}) for query '{query}'")
            
            # Yield a new request for the next page of search results
            yield scrapy.Request(
                url=self.search_url,
                method='POST',
                body=json.dumps(post_data),
                callback=self.parse,
                cb_kwargs={'post_data': post_data},
                errback=lambda failure: self.handle_error(failure, context="pagination_request")
            )

    def parse_job_details(self, response, job_id):
        """
        Parses the job detail response, saves it to a file, and logs the scraping success or failure.
        Handles JSON decoding errors and sends Slack notifications if an error occurs.
        """
        # Generate a filename for the job details using the job ID
        filename = f"{job_id}.json"
        filepath = os.path.join(self.job_detail_path, filename)

        # Save the raw job detail response body to a file
        with open(filepath, 'wb') as f:
            f.write(response.body)
        self.logger.info(f"Saved job details for job ID {job_id} to {filepath}")
        try:
            # Attempt to parse the response body as JSON
            job_details = response.json()
            self.logger.info(f"Successfully scraped job details from {response.url}")
        except json.JSONDecodeError as e:
            self.logger.error(f"Failed to decode JSON from job details response: {response.url}")
            
            # Dump complete failure data
            error_data = {
                "type": "JSONDecodeError",
                "value": str(e),
                "traceback": None,
                "context": "job_details_parsing",
                "job_id": job_id
            }
            
            failure_file = dump_failure_data(
                failure_path=self.failure_path,
                request_data=extract_request_data(response.request),
                response_data=extract_response_data(response),
                error_data=error_data,
                logger=self.logger
            )
            
            # Send Slack notification on JSON decoding failure
            message = (f"Spider '{self.name}' failed to decode JSON from job details response: {response.url}\n"
                      f"Job ID: {job_id}\n"
                      f"Failure data saved to: {failure_file}")
            send_slack_notification(self.logger, self.slack_enabled, self.slack_webhook_url, message, self.name, self.slack_max_notifications)

    def handle_error(self, failure, response=None, **kwargs):
        """
        Handles errors encountered during the scraping process.
        It logs the error, dumps complete failure data, and sends a Slack notification.
        """
        # Try to extract response from HttpError if not provided
        error_response = response
        if not error_response and hasattr(failure, 'value') and hasattr(failure.value, 'response'):
            error_response = failure.value.response
            
        if error_response:
            url = error_response.url
            status = getattr(error_response, 'status', 'Unknown')
            self.logger.error(f"HTTP error {status} for {url}")
            context = "http_error"
        elif response:
            url = response.url
            self.logger.error(f"Unhandled error in spider callback for {url}")
            context = "callback_error"
        else:
            url = failure.request.url if hasattr(failure, 'request') else "Unknown"
            self.logger.error(repr(failure))
            context = "request_error"
        
        # Dump complete failure data, using error_response for HttpErrors
        failure_file = dump_failure_data(
            failure_path=self.failure_path,
            request_data=extract_request_data(getattr(failure, 'request', None)),
            response_data=extract_response_data(error_response) if error_response else None,
            error_data=extract_error_data(failure),
            logger=self.logger
        )
        
        # Determine error context for better categorization
        error_context = kwargs.get('context', context)
        
        if error_response:
            status = getattr(error_response, 'status', 'Unknown')
            reason = getattr(error_response, 'reason', 'Unknown reason')
            # Construct error message including HTTP status and traceback for Slack notification
            message = (f"Spider '{self.name}' encountered HTTP error {status} ({reason}) for {url}.\n"
                       f"Context: {error_context}\n"
                       f"Failure data saved to: {failure_file}\n"
                       f"Traceback: {failure.getTraceback()}")
        elif response:
            # Construct error message including traceback for Slack notification
            message = (f"Spider '{self.name}' encountered an unhandled exception while processing {url}.\n"
                       f"Context: {error_context}\n"
                       f"Response Status: {getattr(response, 'status', 'Unknown')}\n"
                       f"Failure data saved to: {failure_file}\n"
                       f"Traceback: {failure.getTraceback()}")
        else:
            # Construct error message for request-level failures
            message = (f"Scrapy spider '{self.name}' encountered a request error.\n"
                       f"URL: {url}\n"
                       f"Context: {error_context}\n"
                       f"Failure data saved to: {failure_file}\n"
                       f"Traceback: {failure.getTraceback()}")

        send_slack_notification(self.logger, self.slack_enabled, self.slack_webhook_url, message, self.name)
