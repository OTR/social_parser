""""""
from config.settings.common_settings import *

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1"]

STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = "/static/"
