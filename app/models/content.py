"""
username
subscribers
platform
content_id
link
seized_top

"""
from django.db import models
from django.utils import timezone

from domain.vo.content_status import ContentStatus
from domain.vo.content_platform import ContentPlatform


def is_not_blank(value: str):
    return value is not None and value != ""


class ContentModel(models.Model):
    """"""
    _STATUS_CHOICES = [(status.value, status.name) for status in ContentStatus]
    _PLATFORM_CHOICES = [(platform.value, platform.name) for platform in ContentPlatform]

    username = models.CharField(max_length=255, null=True)
    subscribers = models.IntegerField(null=True, blank=True)
    platform = models.CharField(
        max_length=20,
        choices=_PLATFORM_CHOICES,
        default=ContentPlatform.OTHER.value,
    )
    content_id = models.CharField(max_length=255, verbose_name="Content ID", null=True)
    link = models.CharField(max_length=255)
    seized_top = models.BooleanField(verbose_name="seized top", null=True)
    views = models.IntegerField(null=True, blank=True)
    likes = models.IntegerField(null=True, blank=True)
    shares = models.IntegerField(null=True, blank=True)
    comments = models.IntegerField(null=True, blank=True)
    published_at = models.DateTimeField(verbose_name="published at", default=timezone.now())
    title = models.CharField(max_length=255, null=True)
    reason = models.TextField(null=True)
    through_suggestion = models.BooleanField(verbose_name="through suggestion", null=True)
    status = models.CharField(
        max_length=20,
        choices=_STATUS_CHOICES,
        default=ContentStatus.NOT_LABELED.value,
    )

    class Meta:
        """"""
        ordering = ['id']  # Default ordering by 'id'

    def __str__(self):
        """Redefine string representation of a table row in admin site"""
        string_repr: str = ""
        if is_not_blank(str(self.title)):
            string_repr = str(self.title)
        elif is_not_blank(str(self.username)) or is_not_blank(str(self.reason)):
            string_repr = f"{self.username} {self.reason}"
        else:
            string_repr = str(self.link)

        return string_repr
