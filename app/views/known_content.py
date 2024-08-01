""""""
from django.views.generic import ListView

from app.models import ContentModel


class KnownContentView(ListView):
    """"""

    model = ContentModel
    paginate_by = 10
    template_name = "app/known_content.html"
