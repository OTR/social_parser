from config.settings.prod_settings import *

DEBUG = True
ALLOWED_HOSTS = os.getenv('DJANGO_ALLOWED_HOSTS', 'localhost').split(',')

TIME_ZONE = "Etc/GMT-3"  # UTC+3
