from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Profile", {"fields": ("phone", "organization", "job_title")}),
    )
    list_display = ("username", "email", "first_name", "last_name", "organization", "is_staff")
