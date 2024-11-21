"""
Concrete production settings for `pythonanywhere.com`, extend base production
 settings from `prod_settings.py`

Variables with leading "U_" mean user defined settings, not Django's
"""
from config.settings.prod_settings import *

# Your login on hosting
U_LOGIN = os.environ.get("U_LOGIN")
U_DB_PASSWD = os.environ.get("U_DB_PASSWD")
# MySQL table name, creates on a dashboard
U_DB_NAME = os.environ.get("U_DB_NAME")

ALLOWED_HOSTS = [f"{U_LOGIN}.pythonanywhere.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": f"{U_LOGIN}${U_DB_NAME}",
        "HOST": f"{U_LOGIN}.mysql.pythonanywhere-services.com",
        "USER": f"{U_LOGIN}",
        "PASSWORD": f"{U_DB_PASSWD}",
    },
}

TIME_ZONE = "Etc/GMT-3"  # UTC+3
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_DIR = BASE_DIR / "static"
STATICFILES_DIRS = [STATIC_DIR]
STATIC_URL = "/static/"
