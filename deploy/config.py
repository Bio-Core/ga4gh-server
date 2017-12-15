import os
# this file seems to be necessary in order for deployment to work
# without it, ga4gh server starts interpretting file paths as URLs
DATA_SOURCE = os.getenv('GA4GH_DATA_SOURCE', "/srv/ga4gh-compliance-data/registry.db")
DEBUG = os.getenv('GA4GH_DEBUG', "")
