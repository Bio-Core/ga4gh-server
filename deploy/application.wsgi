# This file is copied into place by the .whiskey/action_hooks/pre-build hook during Docker build

from ga4gh.server.frontend.frontend import app as application
import ga4gh.server.frontend.frontend as frontend
frontend.configure("/srv/config.py")
