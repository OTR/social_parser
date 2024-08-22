"""
Concrete production settings for `pythonanywhere.com`, extend base production
 settings from `prod_settings.py`

Variables with leading "U_" mean user defined settings, not Django's
"""
import os

from config.settings.prod_settings import *

# Your login on hosting
U_LOGIN = os.environ.get("U_LOGIN")
U_HOST = os.environ.get("U_HOST")
U_DB_PASSWD = os.environ.get("U_DB_PASSWD")
# MySQL table name, creates on a dashboard
U_TABLE_NAME = "test_targets"

ALLOWED_HOSTS = ["127.0.0.1"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": f"{U_TABLE_NAME}",
        "HOST": f"{U_HOST}",
        "USER": f"{U_LOGIN}",
        "PASSWORD": f"{U_DB_PASSWD}",
    },
}

# TODO: Use ENVIRONMENT VARIABLE instead of hardcoded timezone
TIME_ZONE = "Etc/GMT-3"  # UTC+3
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = "/static/"
