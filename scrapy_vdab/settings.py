# Scrapy settings for scrapy_vdab project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "scrapy_vdab"

SPIDER_MODULES = ["scrapy_vdab.spiders"]
NEWSPIDER_MODULE = "scrapy_vdab.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "scrapy_vdab (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Concurrency and throttling settings
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 16
DOWNLOAD_DELAY = 0.5

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'vej-key-monitor': 'b277002f-e1fa-4fc5-868a-fdab633c3851',
    'content-type': 'application/json',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     # "scrapy_vdab.middlewares.ScrapyVdabSpiderMiddleware": 543,
#
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    "scrapy_vdab.middlewares.ScrapyVdabDownloaderMiddleware": 543,
    # "scrapy_vdab.middlewares.DebugRequestMiddleware": 2000,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_vdab.pipelines.ScrapyVdabPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True
# The initial download delay
AUTOTHROTTLE_START_DELAY = 1
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 30
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 16
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

BASE_DIR = "/app/scrapy_vdab"
DATA_LAKE_DIR = "data/datalake"

# VDAB spider settings
VDAB_SEARCH_QUERIES = ["etl", "powershell", "spark", 'data engineer', 'django', 'vlaanderen connect', 'llm', 'rag',
                       'fast api', 'airflow', 'python', 'llm engineer']
VDAB_SEARCH_CRITERIA = {
    "locatieCriteria": {
        "geoLocatie": {
            "latitude": None,
            "longitude": None
        },
        "locatieCode": "2643",
        "locatiePostcodeGemeente": "9451 Kerksken",
        "straalInKilometer": 30
    },
    "onlineSindsCode": "9000",
    "sorteerVeld": "DATUM",
}

# Slack notifications
SLACK_NOTIFICATIONS_ENABLED = False
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"  # Replace with your actual webhook URL
SLACK_MAX_NOTIFICATIONS_PER_SPIDER = 10  # Maximum Slack notifications per spider run to prevent spam
