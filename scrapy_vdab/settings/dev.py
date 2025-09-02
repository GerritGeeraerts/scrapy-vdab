# Development environment settings for scrapy_vdab project
#
# This file contains development-specific configurations that override
# or extend the base settings for local development.

from .base import *

# ============================================================================
# DEVELOPMENT ENVIRONMENT CONFIGURATION
# ============================================================================

# Base directory for development (local file system)
BASE_DIR = "/home/gg/PycharmProjects/scrapy-vdab/"

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

# Set log level to DEBUG for detailed development logging
LOG_LEVEL = "DEBUG"

# ============================================================================
# CONCURRENCY & PERFORMANCE
# ============================================================================

# Reduce concurrency for development to make debugging easier
# CONCURRENT_REQUESTS = 1
# CONCURRENT_REQUESTS_PER_DOMAIN = 1

# Slower download delay for development to be gentler on target servers
# DOWNLOAD_DELAY = 1.0

# AutoThrottle settings for development
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1
# AUTOTHROTTLE_START_DELAY = 1
# AUTOTHROTTLE_MAX_DELAY = 10

# Enable debug output for AutoThrottle in development
# AUTOTHROTTLE_DEBUG = True

# ============================================================================
# DEVELOPMENT DEBUGGING
# ============================================================================

# Enable HTTP caching for development to speed up testing
HTTPCACHE_ENABLED = True
HTTPCACHE_EXPIRATION_SECS = 3600  # Cache for 1 hour
HTTPCACHE_DIR = "httpcache"
HTTPCACHE_IGNORE_HTTP_CODES = []
HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Enable Telnet Console for development debugging
TELNETCONSOLE_ENABLED = True

# Uncomment to enable debug request middleware for development
# DOWNLOADER_MIDDLEWARES.update({
#     "scrapy_vdab.middlewares.DebugRequestMiddleware": 2000,
# })

# ============================================================================
# SLACK NOTIFICATIONS
# ============================================================================

# Disable Slack notifications in development to avoid spam
SLACK_NOTIFICATIONS_ENABLED = False
