""""""
from django.db import models


class Highlight:
    """"""
    channel_id = models.CharField(max_length=255, verbose_name="Channel id")
    channel_title = models.CharField(max_length=255, verbose_name="Channel title")
    reason = models.TextField()
