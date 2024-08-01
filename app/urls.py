""""""
from django.urls import path
from app.views import IndexView, KnownContentView
import app.apps


app_name = app.apps.AppConfig.name
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("list", KnownContentView.as_view(), name="known_content")
]
