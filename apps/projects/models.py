from django.conf import settings
from django.db import models

from apps.provinces.models import Province
from apps.waste_sites.models import WasteSite


class Project(models.Model):
    """Capital or operational waste-management initiative."""

    class Status(models.TextChoices):
        DRAFT = "draft", "Draft"
        ACTIVE = "active", "Active"
        ON_HOLD = "on_hold", "On hold"
        COMPLETED = "completed", "Completed"
        CANCELLED = "cancelled", "Cancelled"

    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    province = models.ForeignKey(
        Province,
        on_delete=models.PROTECT,
        related_name="projects",
    )
    primary_site = models.ForeignKey(
        WasteSite,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="primary_projects",
    )
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.DRAFT,
    )
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    budget_currency = models.CharField(max_length=3, default="USD")
    budget_amount = models.DecimalField(
        max_digits=14,
        decimal_places=2,
        null=True,
        blank=True,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="owned_projects",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "projects_project"
        ordering = ["-start_date", "name"]

    def __str__(self):
        return f"{self.code} — {self.name}"


class ProjectSite(models.Model):
    """Many-to-many link between projects and waste sites with role."""

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="project_sites",
    )
    waste_site = models.ForeignKey(
        WasteSite,
        on_delete=models.CASCADE,
        related_name="project_links",
    )
    role = models.CharField(
        max_length=64,
        blank=True,
        help_text="e.g. primary, beneficiary, monitoring",
    )

    class Meta:
        db_table = "projects_projectsite"
        unique_together = [("project", "waste_site")]
