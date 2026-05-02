from django.db import models


class Province(models.Model):
    """Top-level administrative region for waste program roll-out."""

    code = models.CharField(max_length=16, unique=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "provinces_province"
        ordering = ["name"]

    def __str__(self):
        return self.name


class District(models.Model):
    """Sub-region within a province (district / municipality)."""

    province = models.ForeignKey(
        Province,
        on_delete=models.CASCADE,
        related_name="districts",
    )
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = "provinces_district"
        unique_together = [("province", "code")]
        ordering = ["province", "name"]

    def __str__(self):
        return f"{self.name} ({self.province.code})"
