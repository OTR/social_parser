""""""
from django.views.generic import ListView

from app.models import ContentModel
from app.models.content_status import ContentStatus


class KnownContentView(ListView):
    """"""
    model = ContentModel
    paginate_by = 10
    template_name = "app/known_content.html"

    def get_queryset(self):
        queryset = super().get_queryset()
        status = self.request.GET.get('status', 'all')  # Get the 'status' parameter from the URL

        if status and status in ContentStatus.all_uri_params():
            if status == ContentStatus.IN_PROGRESS.as_uri():
                queryset = queryset.filter(status=ContentStatus.IN_PROGRESS.value)
            elif status == ContentStatus.TO_DO.as_uri():
                queryset = queryset.filter(status=ContentStatus.TO_DO.value)
            elif status == ContentStatus.DONE.as_uri():
                queryset = queryset.filter(status=ContentStatus.DONE.value)
            elif status == ContentStatus.REJECTED.as_uri():
                queryset = queryset.filter(status=ContentStatus.REJECTED.value)
            elif status == ContentStatus.NOT_LABELED.as_uri():
                queryset = queryset.filter(status=ContentStatus.NOT_LABELED.value)

        return queryset

    def get_context_data(self, **kwargs):
        """"""
        context = super().get_context_data(**kwargs)
        status: str = self.request.GET.get("status", "all")
        context["status"] = status

        return context
