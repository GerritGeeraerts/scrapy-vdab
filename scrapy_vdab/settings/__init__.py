# Settings module for scrapy_vdab project
#
# This module provides environment-specific settings loading.
# The environment is determined by the SCRAPY_ENV environment variable.
#
# Supported environments:
# - development (default): Uses settings/dev.py
# - production: Uses settings/production.py
#
# Usage:
#   export SCRAPY_ENV=production
#   scrapy crawl vdab

import os

# Determine which environment settings to load
environment = os.getenv('SCRAPY_VDAB_ENV', 'dev')

if environment == 'production':
    from .production import *
else:
    from .dev import *

# Make the environment available for debugging
ENVIRONMENT = environment
