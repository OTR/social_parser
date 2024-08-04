import os

import pytz
from django import template
from django.utils import timezone
from datetime import timedelta

from dotenv import load_dotenv

register = template.Library()
load_dotenv()


@register.filter
def time_since(value):
    offset = os.getenv("TIMEZONE_OFFSET")
    local_tz = pytz.timezone("Etc/GMT-" + str(offset))
    value = timezone.make_aware(value, local_tz)
    now = timezone.datetime.now().astimezone(local_tz)
    diff = now - value

    if diff < timedelta(minutes=1):
        return f"{int(diff.seconds)} seconds ago"
    elif diff < timedelta(hours=1):
        return f"{int(diff.seconds // 60)} minutes ago"
    elif diff < timedelta(days=1):
        return f"{int(diff.seconds // 3600)} hours ago"
    elif diff < timedelta(days=7):
        return f"{int(diff.days)} days ago"
    else:
        return value.strftime('%B %d, %Y')  # Format the date if it's more than a week ago
