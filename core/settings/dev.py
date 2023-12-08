from dotenv import load_dotenv

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

load_dotenv()

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY = os.environ.get('SECRET_KEY', "dev-django-insecure-1p-plpfl!0v)3(3iob99#%(x@kf$0i#yuk=&&y7=diok16m7d^")
print(f"{SECRET_KEY=}")



EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

try:
    from .local import *
except ImportError:
    pass
