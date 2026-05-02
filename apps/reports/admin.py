from django.contrib import admin

from .models import ReportDefinition, ReportRun


@admin.register(ReportDefinition)
class ReportDefinitionAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "is_active", "created_at")
    list_filter = ("is_active",)
    prepopulated_fields = {"code": ("name",)}


@admin.register(ReportRun)
class ReportRunAdmin(admin.ModelAdmin):
    list_display = ("definition", "status", "requested_by", "started_at", "finished_at")
    list_filter = ("status", "definition")
    raw_id_fields = ("requested_by",)
    readonly_fields = ("started_at",)
