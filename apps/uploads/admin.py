from django.contrib import admin

from .models import FileAttachment


@admin.register(FileAttachment)
class FileAttachmentAdmin(admin.ModelAdmin):
    list_display = (
        "original_name",
        "purpose",
        "content_type",
        "object_id",
        "uploaded_by",
        "uploaded_at",
    )
    list_filter = ("purpose", "content_type")
    raw_id_fields = ("uploaded_by",)
