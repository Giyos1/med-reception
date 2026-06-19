from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    # Uchta rol bo'lishi mumkin
    ROLE_CHOICES = (
        ('Administrator', 'Administrator'),
        ('Doctor', 'Doctor'),
        ('Patient', 'Patient'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='Patient')
    tel_number = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f"{self.username} ({self.role})"