from django.contrib import admin

from .models import Complaint, ComplaintCategory


@admin.register(ComplaintCategory)
class ComplaintCategoryAdmin(admin.ModelAdmin):
    list_display = ("code", "name")


@admin.register(Complaint)
class ComplaintAdmin(admin.ModelAdmin):
    list_display = (
        "reference",
        "title",
        "category",
        "province",
        "status",
        "reported_at",
    )
    list_filter = ("status", "category", "province")
    search_fields = ("reference", "title", "description")
    raw_id_fields = ("waste_site", "reported_by", "assigned_to")
    readonly_fields = ("reference", "created_at", "updated_at")
