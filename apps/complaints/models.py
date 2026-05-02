from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.provinces.models import Province
from apps.waste_sites.models import WasteSite


class ComplaintCategory(models.Model):
    """Reason / channel grouping for complaints."""

    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "complaints_complaintcategory"
        verbose_name_plural = "Complaint categories"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Complaint(models.Model):
    """Citizen or inspector report linked to geography and optional site."""

    class Status(models.TextChoices):
        NEW = "new", "New"
        IN_REVIEW = "in_review", "In review"
        ASSIGNED = "assigned", "Assigned"
        RESOLVED = "resolved", "Resolved"
        CLOSED = "closed", "Closed"

    reference = models.CharField(max_length=32, unique=True, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(
        ComplaintCategory,
        on_delete=models.PROTECT,
        related_name="complaints",
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.PROTECT,
        related_name="complaints",
    )
    waste_site = models.ForeignKey(
        WasteSite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="complaints",
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.NEW,
    )
    reported_at = models.DateTimeField(default=timezone.now)
    reported_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="reported_complaints",
    )
    assigned_to = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="assigned_complaints",
    )
    resolution_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "complaints_complaint"
        ordering = ["-reported_at"]

    def __str__(self):
        return f"{self.reference} — {self.title}"

    def save(self, *args, **kwargs):
        if not self.reference:
            from uuid import uuid4

            self.reference = uuid4().hex[:12].upper()
        super().save(*args, **kwargs)
