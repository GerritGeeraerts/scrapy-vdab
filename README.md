# VDAB Job Scraper with 🕸️ Scrapy 🕸️
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Scrapy](https://img.shields.io/badge/Scrapy-4E9A00?style=for-the-badge&logo=spider&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![JSON](https://img.shields.io/badge/json-5E5C5C?style=for-the-badge&logo=json&logoColor=white)


## 🔍 Description
Professional web scraper for extracting job listings from VDAB.be (Flemish Public Employment Service). This Scrapy-based project searches for specific tech-related jobs in Belgium and systematically extracts comprehensive job data including detailed descriptions, requirements, company information, and employment conditions. Perfect for job market analysis, career research, or building job recommendation systems.

## 📦 Repo structure
```
├── scrapy_vdab/
│   ├── spiders/
│   │   └── vdab.py              # Main spider for job scraping
│   ├── data/
│   │   └── datalake/            # Structured data storage (bronze layer)
│   │       └── projects/jobs/bronze/vdab/
│   │           ├── job_searches/    # Raw search results by date
│   │           ├── job_listings/    # Individual job details
│   │           └── failures/        # Error logs and debugging data
│   ├── assets/
│   │   └── example_failure_dump.json  # Sample failure data structure
│   ├── settings.py              # Scrapy configuration & spider settings
│   ├── items.py                 
│   ├── middlewares.py           
│   ├── pipelines.py             
│   ├── utils.py                 # Utility functions (Slack, error handling)
│   ├── docs-endpoint-detail.md  # API documentation for job details
│   └── docs-endpoint-zoek.md    # API documentation for job search
├── Dockerfile                   # Container configuration
├── requirements.txt             # Python dependencies
└── scrapy.cfg                   # Scrapy project configuration
```
### Job Details Structure
Individual job data stored as:
```
data/datalake/projects/jobs/bronze/vdab/job_listings/
└── year=2024/month=01/day=15/
    ├── 71780743.json           # Complete job posting data
    └── 71829072.json           # Another job posting
```

## 🔍 API Endpoints

The spider interacts with VDAB's REST API:

### Job Search
- **Endpoint**: `POST https://www.vdab.be/rest/vindeenjob/v4/vacatureLight/zoek`
- **Purpose**: Search for jobs matching specific criteria
- **Documentation**: [docs-endpoint-zoek.md](scrapy_vdab/docs-endpoint-zoek.md)

### Job Details  
- **Endpoint**: `GET https://www.vdab.be/rest/vindeenjob/v4/vacatures/{id}`
- **Purpose**: Retrieve complete job posting information
- **Documentation**: [docs-endpoint-detail.md](scrapy_vdab/docs-endpoint-detail.md)

## ⚙️ Advanced Configuration

### Slack Notifications
Enable real-time error notifications:
```python
SLACK_NOTIFICATIONS_ENABLED = True
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"
SLACK_MAX_NOTIFICATIONS_PER_SPIDER = 10
```

### Throttling & Rate Limiting
Built-in respect for server resources:
```python
DOWNLOAD_DELAY = 0.5
AUTOTHROTTLE_ENABLED = True
CONCURRENT_REQUESTS_PER_DOMAIN = 16
```

### Custom Search Criteria
Modify geographic and timing filters:
```python
VDAB_SEARCH_CRITERIA = {
    "locatieCriteria": {
        "locatieCode": "2643",
        "locatiePostcodeGemeente": "9451 Kerksken", 
        "straalInKilometer": 30
    },
    "onlineSindsCode": "9000",  # All jobs
    "sorteerVeld": "DATUM"
}
```

## 🐛 Debugging & Monitoring

### Failure Analysis
Failed requests generate comprehensive debug files:
```json
{
  "timestamp": "2024-01-15T10:30:00",
  "request": {
    "url": "https://www.vdab.be/rest/...",
    "method": "POST",
    "headers": {...},
    "body": "..."
  },
  "response": {
    "status": 500,
    "headers": {...},
    "body": "..."
  },
  "error": {
    "type": "HTTPError",
    "traceback": "..."
  }
}
```

### Log Levels
Run with different verbosity:
```bash
scrapy crawl vdab -L INFO   # Standard logging
scrapy crawl vdab -L DEBUG  # Verbose debugging
scrapy crawl vdab -L ERROR  # Errors only
```


## 🚀 Getting Started

### 📋 Prerequisites
Before running the spider, ensure you have Python 3.11+ installed.

### 💾 Install requirements
```bash
pip install -r requirements.txt
```

### 🔧 Configuration
You can modify search queries in `scrapy_vdab/settings.py`, I did not scrape all jobs, as this is just a demonstration project. You can add your own keywords here:
```python
VDAB_SEARCH_QUERIES = ["etl", "data engineer", "sql"]
```

### 🏃‍♂️ Run the Spider
Execute the spider to start scraping job listings:

```bash
cd scrapy_vdab
scrapy crawl vdab
```

### 🐳 Docker Deployment
For containerized deployment:

```bash
# Manually create a Docker volume for data persistence
docker volume create datalake

# Build the image
docker build -t scrapy-vdab .

# Run with data persistence
docker run -v datalake:/app/scrapy_vdab/data/datalake scrapy-vdab

# Interactive mode for debugging
docker run -it scrapy-vdab /bin/bash
```

## 🔧 Features

### 🎯 Smart Job Search
- **Multi-keyword Search**: Searches multiple tech-related terms simultaneously
- **Geographic Filtering**: Focuses on jobs within 30km of Kerksken, Belgium
- **Pagination Handling**: Automatically processes all result pages
- **Duplicate Detection**: Identifies and handles duplicate job listings

### 🛡️ Robust Error Handling
- **Failure Recovery**: Comprehensive error logging and debugging data
- **Request Retry**: Automatic retry mechanisms for failed requests
- **Data Validation**: JSON parsing with fallback error handling
- **Slack Integration**: Real-time notifications for critical failures

### 🗂️ Data Lake Architecture
Implements a structured data lake with:
- **Bronze Layer**: Raw data storage organized by date
- **Partitioned Storage**: Year/Month/Day folder structure
- **Format Preservation**: Original JSON responses maintained
- **Failure Tracking**: Complete request/response/error data for debugging

## ⏱️ Timeline
I was able to complete this project in 1 day, having experience of web scraping and combined them with knowledge of my data engineering course.

## 🤝 Contributing
Feel free to submit issues and enhancement requests. This scraper follows ethical scraping practices with built-in rate limiting and respectful request patterns.

### Connect with me!
[![LinkedIn](https://img.shields.io/badge/linkedin-%230077B5.svg?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/gerrit-geeraerts-143488141)
[![Stack Overflow](https://img.shields.io/badge/-Stackoverflow-FE7A16?style=for-the-badge&logo=stack-overflow&logoColor=white)](https://stackoverflow.com/users/10213635/gerrit-geeraerts)
[![Ask Ubuntu](https://img.shields.io/badge/Ask%20Ubuntu-dc461d?style=for-the-badge&logo=linux&logoColor=black)](https://askubuntu.com/users/1097288/gerrit-geeraerts)