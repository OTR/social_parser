""""""
from django.views.generic import TemplateView
from service.youtube import YoutubeApiClient


class NewContentView(TemplateView):
    """"""
    template_name = "app/new.html"

    def get_context_data(self, **kwargs) -> dict:
        """Just a stub function to be modified later."""
        context: dict = super().get_context_data(**kwargs)

        youtube_dto = YoutubeApiClient().get_latest_videos()

        context["youtube_dto"] = youtube_dto

        return context
