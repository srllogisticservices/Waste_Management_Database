from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class FileAttachment(models.Model):
    """Polymorphic file storage for complaints, sites, reports, etc."""

    class Purpose(models.TextChoices):
        EVIDENCE = "evidence", "Evidence"
        SITE_PHOTO = "site_photo", "Site photo"
        REPORT_OUTPUT = "report_output", "Report output"
        GENERAL = "general", "General"

    file = models.FileField(upload_to="attachments/%Y/%m/")
    original_name = models.CharField(max_length=255, blank=True)
    mime_type = models.CharField(max_length=128, blank=True)
    size_bytes = models.PositiveIntegerField(null=True, blank=True)
    purpose = models.CharField(
        max_length=32,
        choices=Purpose.choices,
        default=Purpose.GENERAL,
    )
    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.PositiveBigIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="uploads",
    )
    uploaded_at = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "uploads_fileattachment"
        ordering = ["-uploaded_at"]
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
