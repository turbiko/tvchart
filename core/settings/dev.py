from dotenv import load_dotenv

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1p-plpfl!0v)3(3iob99#%(x@kf$0i#yuk=&&y7=diok16m7d^"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
