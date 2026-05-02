from django.contrib import admin

from .models import Project, ProjectSite


class ProjectSiteInline(admin.TabularInline):
    model = ProjectSite
    extra = 0
    raw_id_fields = ("waste_site",)


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("code", "name", "province", "status", "start_date", "owner")
    list_filter = ("status", "province")
    search_fields = ("code", "name", "description")
    raw_id_fields = ("primary_site", "owner")
    inlines = [ProjectSiteInline]
