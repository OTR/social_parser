""""""
from django.contrib import admin
from django.contrib.auth.models import Group, User

from app.models import ContentModel, HighlightModel


class ContentModelAdmin(admin.ModelAdmin):
    """"""
    readonly_fields = ("id",)


class HightlighterModelAdmin(admin.ModelAdmin):
    """"""
    readonly_fields = ("id",)


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.register(ContentModel, ContentModelAdmin)
admin.site.register(HighlightModel, HightlighterModelAdmin)
