"""
WSGI config for vercel_app project.

It exposes the WSGI callable as a module-level variable named ``app``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

settings_module = 'mysite.production' if 'WEBSITE_HOSTNAME' in os.environ else 'mysite.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

# 21-10-2025 - For Azure - "application" match in asgi.py as well as in settings "WSGI_APPLICATION"
application = get_wsgi_application()
