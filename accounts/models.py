from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('project_manager', 'Project Manager'),
        ('customer', 'Customer'),
        ('agency_member', 'Agency Member'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15)
    organization = models.CharField(max_length=100, blank=True)

    def __str__(self) -> str:
        return f"{self.username} ({self.role})"
