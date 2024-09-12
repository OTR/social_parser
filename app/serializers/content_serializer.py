"""
"""
from rest_framework import serializers
from app.models import ContentModel


class ContentModelSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        """"""
        model = ContentModel
        fields = [
            "username", "subscribers", "platform", "content_id", "link", "seized_top",
            "views", "likes", "shares", "comments", "published_at", "title", "reason",
            "through_suggestion", "status"
        ]
