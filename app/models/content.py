""""""
from django.db import models
from django.utils import timezone


class ContentModel(models.Model):
    """"""
    username = models.CharField(max_length=255, null=True)
    subscribers = models.IntegerField(null=True)
    link = models.CharField(max_length=255)
    seized_top = models.BooleanField(verbose_name="seized top", null=True)
    views = models.IntegerField(null=True)
    shares = models.IntegerField(null=True)
    comments = models.IntegerField(null=True)
    added_date = models.DateTimeField(verbose_name="added date", default=timezone.now())
    title = models.CharField(max_length=255, null=True)
    reason = models.TextField(null=True)
    through_suggestion = models.BooleanField(verbose_name="through suggestion", null=True)

    def __str__(self):
        """Redefine string representation of a table row in admin site"""
        string_repr: str = ""
        if self.title is None:
            string_repr = f"{self.username} {self.reason}"
        else:
            string_repr = str(self.title)

        return string_repr
