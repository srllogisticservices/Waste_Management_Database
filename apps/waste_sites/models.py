from django.conf import settings
from django.db import models

from apps.provinces.models import District, Province


class WasteSiteType(models.Model):
    """Classification: landfill, transfer station, MRF, illegal dump, etc."""

    code = models.CharField(max_length=32, unique=True)
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)

    class Meta:
        db_table = "waste_sites_wastesitetype"
        ordering = ["name"]

    def __str__(self):
        return self.name


class WasteSite(models.Model):
    """Physical waste handling or disposal location."""

    class OperationalStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        PLANNED = "planned", "Planned"
        CLOSED = "closed", "Closed"

    name = models.CharField(max_length=255)
    site_type = models.ForeignKey(
        WasteSiteType,
        on_delete=models.PROTECT,
        related_name="sites",
    )
    province = models.ForeignKey(
        Province,
        on_delete=models.PROTECT,
        related_name="waste_sites",
    )
    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="waste_sites",
    )
    address = models.TextField(blank=True)
    latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        null=True,
        blank=True,
    )
    operational_status = models.CharField(
        max_length=16,
        choices=OperationalStatus.choices,
        default=OperationalStatus.ACTIVE,
    )
    capacity_notes = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="created_waste_sites",
    )

    class Meta:
        db_table = "waste_sites_wastesite"
        ordering = ["name"]

    def __str__(self):
        return self.name
