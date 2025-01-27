from django.views.generic import TemplateView


class IndexView(TemplateView):
    """A view to display root page of the site."""

    template_name = "app/base.html"
