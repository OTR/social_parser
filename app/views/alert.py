""""""
import os

from dotenv import load_dotenv

from django.views.generic import TemplateView

load_dotenv()


class AlertView(TemplateView):
    """"""
    template_name = "app/alert.html"

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        youtube_cooldown = int(os.getenv("YOUTUBE_COOL_DOWN_IN_MINUTES", "10"))
        yt_cooldown_in_millis = youtube_cooldown * 1000
        context["youtube_cooldown"] = yt_cooldown_in_millis

        return context
