from django.contrib import admin
from . import models


@admin.register(models.SiteInfo)
class SiteInfoAdmin(admin.ModelAdmin):
    exclude = ("manifest",)

    def has_add_permission(self, request, obj=None):
        if models.SiteInfo.objects.count() > 0:
            return False
        else:
            return True


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    def has_add_permission(self, request, obj=None):
        if models.Author.objects.count() > 0:
            return False
        else:
            return True
