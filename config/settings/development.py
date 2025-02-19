from .base import *

DEBUG = True

# Allow all hosts in development
ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# CORS settings
CORS_ORIGIN_ALLOW_ALL = True
