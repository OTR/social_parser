from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import ContentModel, HighlightModel


@admin.register(ContentModel)
class ContentModelAdmin(admin.ModelAdmin):
    """"""
    readonly_fields = ("id",)
    list_filter = ("status", )
    search_fields = ["content_id",]


@admin.register(HighlightModel)
class HightlighterModelAdmin(admin.ModelAdmin):
    """"""
    readonly_fields = ("id",)


admin.site.unregister(Group)
admin.site.unregister(User)
