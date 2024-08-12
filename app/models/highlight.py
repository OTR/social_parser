""""""
from django.db import models
from django.utils import timezone


class HighlightModel(models.Model):
    """"""
    channel_id = models.CharField(max_length=255, unique=True, verbose_name="Channel id")
    channel_title = models.CharField(max_length=255, verbose_name="Channel title", null=True)
    added_date = models.DateTimeField(verbose_name="added date", default=timezone.now())
    reason = models.TextField(null=True)

    class Meta:
        """"""
        ordering = ['id']  # Default ordering by 'id'

    def __str__(self):
        """"""
        return str(self.channel_title)
