""""""
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from service.youtube import YoutubeApiClient
from app.models import HighlightModel, ContentModel
from app.models.content_platform import ContentPlatform


class NewContentApiView(APIView):
    """"""

    def get(self, request, *args, **kwargs):
        """"""
        youtube_dto = YoutubeApiClient().get_latest_videos()
        # Get the list of channel IDs to filter out
        blocked_channels = HighlightModel.objects.values_list('channel_id', flat=True)
        # Get the list of content IDs and platforms to filter out
        existing_content_ids = (ContentModel.objects
                                .filter(platform=ContentPlatform.YOUTUBE.value)
                                .values_list('content_id', flat=True))
        # Filter out the videos from the blocked channels and those already in ContentModel
        filtered_videos = [
            video for video in youtube_dto.entities
            if video.channel_id not in blocked_channels and video.video_id not in existing_content_ids
        ]

        has_new_content: bool = len(filtered_videos) > 0

        return Response(
            {
                "data": [],
                "has_new_content": has_new_content
            },
            status=status.HTTP_200_OK
        )
