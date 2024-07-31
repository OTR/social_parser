""""""
from django.urls import path
from app.views import IndexView
import app.apps


app_name = app.apps.AppConfig.name
urlpatterns = [
    path("", IndexView.as_view(), name="index"),
]
