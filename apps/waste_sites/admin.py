from django.contrib import admin

from .models import WasteSite, WasteSiteType


@admin.register(WasteSiteType)
class WasteSiteTypeAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")


@admin.register(WasteSite)
class WasteSiteAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "site_type",
        "province",
        "district",
        "operational_status",
        "updated_at",
    )
    list_filter = ("operational_status", "site_type", "province")
    search_fields = ("name", "address")
    raw_id_fields = ("created_by",)
