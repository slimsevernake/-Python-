from django.contrib import admin
from django.contrib.sites.models import Site

from .models import SiteConfig


class SiteConfigInline(admin.StackedInline):
    model = SiteConfig
    can_delete = False


class SiteConfigAdmin(admin.ModelAdmin):
    inlines = (SiteConfigInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(SiteConfigAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(Site)
admin.site.register(Site, SiteConfigAdmin)