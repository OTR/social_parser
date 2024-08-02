""""""
from django.views.generic import TemplateView


class NewContentView(TemplateView):
    """"""
    template_name = "app/new.html"

    def get_context_data(self, **kwargs) -> dict:
        """Just a stub function to be modified later."""
        context = super().get_context_data(**kwargs)

        return context

