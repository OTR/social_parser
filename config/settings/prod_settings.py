"""
Base settings for production use, DO NOT USE IT AS IS, any concrete
production settings should extend this settings file.

See: https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/
"""
import os

from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

from config.settings.common_settings import *

PATH_TO_ENVIRONMENT_VARIABLES = Path(__file__).parent.parent.parent / "prod.env"
load_dotenv(PATH_TO_ENVIRONMENT_VARIABLES)

def change_it() -> None:
    """
    Run `python -c 'from django.core.management.utils import
    get_random_secret_key; print(get_random_secret_key())'`
    to generate a new secret key.
    """
    raise ImproperlyConfigured("The SECRET_KEY setting must not be empty.")


ALLOWED_HOSTS = []
DEBUG = False
SECRET_KEY = os.getenv("SECRET_KEY") or change_it()
