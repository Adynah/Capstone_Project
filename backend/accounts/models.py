from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='customer')
    phone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.username} ({self.role})"

