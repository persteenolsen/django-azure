"""
ASGI config for vercel_app project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 21-10-2025 - For Azure - "application" match in wsgi.py as well as in settings "WSGI_APPLICATION"
application = get_asgi_application()
