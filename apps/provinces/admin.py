from django.contrib import admin

from .models import District, Province


class DistrictInline(admin.TabularInline):
    model = District
    extra = 0


@admin.register(Province)
class ProvinceAdmin(admin.ModelAdmin):
    list_display = ("code", "name")
    search_fields = ("code", "name")
    inlines = [DistrictInline]


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "province")
    list_filter = ("province",)
    search_fields = ("code", "name")
