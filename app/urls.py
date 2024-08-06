""""""
from django.urls import path
from app.views import AlertView, IndexView, KnownContentView, NewContentView
from app.views.api import NewContentApiView, add_highlighter
import app.apps


app_name = app.apps.AppConfig.name

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("list", KnownContentView.as_view(), name="known_content"),
    path("new", NewContentView.as_view(), name="new_content"),
    path("alert", AlertView.as_view(), name="alert"),
    path("api/new", NewContentApiView.as_view(), name="check_new_content"),
    path("api/add/highlighter/", add_highlighter, name="add_highlighter")
]
