from dotenv import load_dotenv

from .base import *

DEBUG = False
print(f"Running production config: {DEBUG=}")

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

load_dotenv()


try:
    from .local import *
except ImportError:
    pass
