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
    """
    Represents content metadata stored in the system. This model is designed to manage and
    persist information related to various types of content published on different platforms.

    Attributes:
        username (str): The name of the user or channel associated with the content.
            Optional, can be null.
        subscribers (int): The number of subscribers or followers the user or channel has.
            Optional, can be null or blank.
        platform (str): The platform on which the content is published. Choices are defined
            by the `ContentPlatform` enum. Defaults to 'OTHER'.
        content_id (str): A unique identifier for the content. Optional, can be null.
        link (str): The URL link to the content.
        seized_top (bool): Indicates if the content was seized at the top (e.g., trending).
            Optional, can be null.
        views (int): The number of views the content has received. Optional, can be null or blank.
        likes (int): The number of likes the content has received. Optional, can be null or blank.
        shares (int): The number of times the content has been shared. Optional, can be null or blank.
        comments (int): The number of comments on the content. Optional, can be null or blank.
        published_at (datetime): The date and time when the content was published. Defaults to
            the current time.
        title (str): The title of the content. Optional, can be null.
        reason (str): A text field to store the reason or description associated with the content.
            Optional, can be null.
        through_suggestion (bool): Indicates if the content was suggested through some algorithm or
            recommendation engine. Optional, can be null.
        status (str): The status of the content, as defined by the `ContentStatus` enum. Defaults
            to 'NOT_LABELED'.
    """
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
        unique_together = ('content_id', 'platform')

    def __str__(self):
        """Redefine string representation of a table row in admin site"""
        if is_not_blank(str(self.title)):
            string_repr = str(self.title)
        elif is_not_blank(str(self.username)) or is_not_blank(str(self.reason)):
            string_repr = f"{self.username} {self.reason}"
        else:
            string_repr = str(self.link)

        return string_repr
