""""""
from config.settings.common_settings import *

DEBUG = True
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]

STATIC_ROOT = BASE_DIR / "static"
STATIC_URL = "/static/"

TIME_ZONE = "Etc/GMT-3"  # UTC+3
