"""
WSGI config for pizaid project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import sys

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pizaid.settings")
sys.path.append("~/GitHub/pizaid-interface/pizaid")
sys.path.append("/home/pi/pizaid/pizaid-interface/pizaid")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
