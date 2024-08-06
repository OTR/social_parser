""""""
from rest_framework import serializers
from app.models import HighlightModel


class HighlightModelSerializer(serializers.ModelSerializer):
    """"""

    class Meta:
        """"""
        model = HighlightModel
        fields = ["channel_id", "channel_title", "added_date", "reason"]
