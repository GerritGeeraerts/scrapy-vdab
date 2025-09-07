# Base Scrapy settings for scrapy_vdab project
#
# This file contains common settings shared across all environments.
# Environment-specific settings are defined in dev.py and production.py
#
# For more settings see:
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# ============================================================================
# PROJECT CONFIGURATION
# ============================================================================

BOT_NAME = "scrapy_vdab"

SPIDER_MODULES = ["scrapy_vdab.spiders"]
NEWSPIDER_MODULE = "scrapy_vdab.spiders"

ADDONS = {}

# ============================================================================
# ROBOT COMPLIANCE & USER AGENT
# ============================================================================

# Obey robots.txt rules (disabled for this scraper)
ROBOTSTXT_OBEY = False

# Custom user agent to mimic a real browser
#USER_AGENT = "scrapy_vdab (+http://www.yourdomain.com)"

# ============================================================================
# REQUEST HEADERS
# ============================================================================

# Override the default request headers to mimic browser requests
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:142.0) Gecko/20100101 Firefox/142.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive',
    'vej-key-monitor': 'b277002f-e1fa-4fc5-868a-fdab633c3851',
    'content-type': 'application/json',
}

# ============================================================================
# CONCURRENCY & RATE LIMITING
# ============================================================================

# Base concurrency settings (overridden in environment-specific files)
#CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 16
DOWNLOAD_DELAY = 0.5

# AutoThrottle extension configuration
AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_START_DELAY = 1  # Initial download delay
AUTOTHROTTLE_MAX_DELAY = 30   # Maximum download delay for high latencies
AUTOTHROTTLE_TARGET_CONCURRENCY = 16  # Average parallel requests per server
#AUTOTHROTTLE_DEBUG = False

# ============================================================================
# COOKIES & TELNET
# ============================================================================

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# ============================================================================
# MIDDLEWARES
# ============================================================================

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

# ============================================================================
# EXTENSIONS
# ============================================================================

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# ============================================================================
# ITEM PIPELINES
# ============================================================================

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "scrapy_vdab.pipelines.ScrapyVdabPipeline": 300,
#}

# ============================================================================
# HTTP CACHING
# ============================================================================

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# ============================================================================
# DATA EXPORT
# ============================================================================

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

# Data storage directory (relative to BASE_DIR)
DATA_LAKE_DIR = "data/datalake"

# ============================================================================
# VDAB SPIDER CONFIGURATION
# ============================================================================

# Search queries for job scraping
VDAB_SEARCH_QUERIES = [
    "etl", 
    "powershell", 
    "spark", 
    "data engineer", 
    "django", 
    "vlaanderen connect", 
    "llm", 
    "rag",
    "fast api", 
    "airflow", 
    "python", 
    "llm engineer",
    "langchain",
    "langgraph",
    "langsmith",
    "scrapy",
    "selenium",
    "playwright",
]

# Search criteria for location and filtering
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

# ============================================================================
# SLACK NOTIFICATIONS
# ============================================================================

# Slack notification settings
SLACK_NOTIFICATIONS_ENABLED = False
SLACK_WEBHOOK_URL = "https://hooks.slack.com/services/YOUR/WEBHOOK/URL"  # Replace with your actual webhook URL
SLACK_MAX_NOTIFICATIONS_PER_SPIDER = 10  # Maximum Slack notifications per spider run to prevent spam
