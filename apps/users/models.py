from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Application user; extends Django auth with domain fields."""

    phone = models.CharField(max_length=32, blank=True)
    organization = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=128, blank=True)

    class Meta:
        db_table = "users_user"
