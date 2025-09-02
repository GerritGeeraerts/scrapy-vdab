# Production environment settings for scrapy_vdab project
#
# This file contains production-specific configurations that override
# or extend the base settings for deployment in production environment.

from .base import *

# ============================================================================
# PRODUCTION ENVIRONMENT CONFIGURATION
# ============================================================================

# Base directory for production (Docker container)
BASE_DIR = "/app/scrapy_vdab"

# ============================================================================
# LOGGING CONFIGURATION
# ============================================================================

# Set log level to INFO for production (less verbose than DEBUG)
LOG_LEVEL = "INFO"

# ============================================================================
# CONCURRENCY & PERFORMANCE
# ============================================================================

# Production concurrency settings for optimal performance
CONCURRENT_REQUESTS = 16
CONCURRENT_REQUESTS_PER_DOMAIN = 16

# Standard download delay for production
DOWNLOAD_DELAY = 0.5

# AutoThrottle settings for production
AUTOTHROTTLE_TARGET_CONCURRENCY = 16
AUTOTHROTTLE_START_DELAY = 1
AUTOTHROTTLE_MAX_DELAY = 30

# Disable debug output for AutoThrottle in production
AUTOTHROTTLE_DEBUG = False

# ============================================================================
# PRODUCTION SECURITY & STABILITY
# ============================================================================

# Disable HTTP caching in production to ensure fresh data
HTTPCACHE_ENABLED = False

# Disable Telnet Console in production for security
TELNETCONSOLE_ENABLED = False

# Disable cookies to prevent session issues in production
COOKIES_ENABLED = False

# ============================================================================
# SLACK NOTIFICATIONS
# ============================================================================

# Enable Slack notifications in production for monitoring
SLACK_NOTIFICATIONS_ENABLED = True

# Production-specific Slack settings
SLACK_MAX_NOTIFICATIONS_PER_SPIDER = 5  # Reduced for production to prevent spam
