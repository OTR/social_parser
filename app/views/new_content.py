""""""
from django.views.generic import TemplateView

from app.models.highlight import HighlightModel
from app.models.content import ContentModel
from service.youtube import YoutubeApiClient


class NewContentView(TemplateView):
    """"""
    template_name = "app/new.html"

    def get_context_data(self, **kwargs) -> dict:
        """Just a stub function to be modified later."""
        context: dict = super().get_context_data(**kwargs)
        next_page_token: str = self.request.GET.get("next_page_token", None)
        prev_page_token: str = self.request.GET.get("prev_page_token", None)

        page_token: str = ""
        if next_page_token is not None and prev_page_token is None:
            page_token = next_page_token
        elif next_page_token is None and prev_page_token is not None:
            page_token = prev_page_token

        youtube_dto = YoutubeApiClient().get_latest_videos(page_token=page_token)

        # Get the list of channel IDs to filter out
        blocked_channels = HighlightModel.objects.values_list('channel_id', flat=True)

        # Get the list of content IDs and platforms to filter out
        existing_content_ids = ContentModel.objects.filter(platform='youtube').values_list('content_id', flat=True)

        # Filter out the videos from the blocked channels and those already in ContentModel
        filtered_videos = [
            video for video in youtube_dto.entities
            if video.channel_id not in blocked_channels and video.video_id not in existing_content_ids
        ]
        youtube_dto.entities = filtered_videos
        context["youtube_dto"] = youtube_dto
        return context
