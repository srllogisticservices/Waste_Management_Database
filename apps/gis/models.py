from django.conf import settings
from django.db import models

from apps.waste_sites.models import WasteSite


class GisLayer(models.Model):
    """Published map layer metadata (WMS/WFS/vector tiles or internal layer id)."""

    class LayerType(models.TextChoices):
        WMS = "wms", "WMS"
        WFS = "wfs", "WFS"
        VECTOR_TILES = "vector_tiles", "Vector tiles"
        GEOJSON = "geojson", "GeoJSON"
        INTERNAL = "internal", "Internal"

    name = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    layer_type = models.CharField(
        max_length=32,
        choices=LayerType.choices,
        default=LayerType.INTERNAL,
    )
    url = models.URLField(blank=True)
    style_json = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    waste_site = models.ForeignKey(
        WasteSite,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="gis_layers",
        help_text="Optional: layer scoped to one site.",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "gis_gislayer"
        ordering = ["name"]

    def __str__(self):
        return self.name


class MapViewState(models.Model):
    """Saved map extent / filters per user (optional UX persistence)."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="map_view_states",
    )
    name = models.CharField(max_length=128, blank=True)
    center_lat = models.DecimalField(max_digits=9, decimal_places=6)
    center_lng = models.DecimalField(max_digits=9, decimal_places=6)
    zoom_level = models.PositiveSmallIntegerField(default=10)
    visible_layer_slugs = models.JSONField(default=list, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "gis_mapviewstate"
        ordering = ["-updated_at"]
