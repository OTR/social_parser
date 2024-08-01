""""""
from django.views.generic import ListView

from app.models import ContentModel


class KnownContentView(ListView):
    """"""

    model = ContentModel
    template_name = "app/known_content.html"
