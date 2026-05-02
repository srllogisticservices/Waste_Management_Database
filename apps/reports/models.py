from django.conf import settings
from django.db import models


class ReportDefinition(models.Model):
    """Registered report template (query + layout parameters)."""

    code = models.SlugField(unique=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    parameter_schema = models.JSONField(
        default=dict,
        blank=True,
        help_text="JSON Schema or ad-hoc keys for filters (province, date range, …).",
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "reports_reportdefinition"
        ordering = ["name"]

    def __str__(self):
        return self.name


class ReportRun(models.Model):
    """Execution record: who ran which report, when, and where output lives."""

    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        RUNNING = "running", "Running"
        SUCCESS = "success", "Success"
        FAILED = "failed", "Failed"

    definition = models.ForeignKey(
        ReportDefinition,
        on_delete=models.CASCADE,
        related_name="runs",
    )
    requested_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name="report_runs",
    )
    parameters = models.JSONField(default=dict, blank=True)
    status = models.CharField(
        max_length=16,
        choices=Status.choices,
        default=Status.PENDING,
    )
    output_file = models.FileField(upload_to="reports/%Y/%m/", blank=True)
    error_message = models.TextField(blank=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = "reports_reportrun"
        ordering = ["-started_at"]
