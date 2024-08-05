""""""
from django.db import models


class HighlightModel(models.Model):
    """"""
    channel_id = models.CharField(max_length=255, verbose_name="Channel id")
    channel_title = models.CharField(max_length=255, verbose_name="Channel title", null=True)
    reason = models.TextField(null=True)

    class Meta:
        """"""
        ordering = ['id']  # Default ordering by 'id'

    def __str__(self):
        """"""
        return str(self.channel_title)
