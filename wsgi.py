import os
from django.core.wsgi import get_wsgi_application
from backend.settings import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
