from dotenv import load_dotenv

from .base import *

DEBUG = True
print(f"Running production config: {DEBUG=}")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

load_dotenv()

ALLOWED_HOSTS = [
    "10.1.100.173",
    "127.0.0.1",
    "localhost",
    "otv.argentum.ua",
    "otv.media",
]

SECRET_KEY = os.environ.get('SECRET_KEY', "django-production-1p-plpfl!0v)3(3iob99#%(x@kf$0i#yuk=&&y7=diok16m7d^")
print(f"{SECRET_KEY=}")

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases
DATABASE_NAME = os.environ.get('DATABASE_NAME')
DATABASE_USER = os.environ.get('DATABASE_USER')
DATABASE_PASSWORD = os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST = os.environ.get('DATABASE_HOST')
# print(f"{DATABASE_NAME=}\n {DATABASE_USER=}\n {DATABASE_HOST=}\n {DATABASE_PASSWORD=}")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
    }
}

CSRF_TRUSTED_ORIGINS = [
    'http://10.1.100.173',
    'http://127.0.0.1',
    'http://localhost',
    'https://otv.argentum.ua',
    'https://otv.media',
]

try:
    from .local import *
except ImportError:
    pass
