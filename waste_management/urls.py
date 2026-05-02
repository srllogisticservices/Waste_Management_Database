"""URL configuration for waste_management project."""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/provinces/", include("apps.provinces.urls")),
    path("api/waste-sites/", include("apps.waste_sites.urls")),
    path("api/complaints/", include("apps.complaints.urls")),
    path("api/projects/", include("apps.projects.urls")),
    path("api/gis/", include("apps.gis.urls")),
    path("api/reports/", include("apps.reports.urls")),
    path("api/uploads/", include("apps.uploads.urls")),
    path("api/users/", include("apps.users.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
