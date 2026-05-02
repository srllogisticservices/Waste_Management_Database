from django.contrib import admin

from .models import GisLayer, MapViewState


@admin.register(GisLayer)
class GisLayerAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "layer_type", "is_active", "waste_site")
    list_filter = ("layer_type", "is_active")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "slug")


@admin.register(MapViewState)
class MapViewStateAdmin(admin.ModelAdmin):
    list_display = ("user", "name", "zoom_level", "updated_at")
    raw_id_fields = ("user",)
