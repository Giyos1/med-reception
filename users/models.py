from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # Username o'rniga telefon raqamidan foydalanamiz
    phone_number = models.CharField(max_length=15, unique=True)

    # Foydalanuvchi rollari
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('shifokor', 'Shifokor'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='shifokor')

    USERNAME_FIELD = 'phone_number'  # Tizimga kirish
    REQUIRED_FIELDS = ['username']  # Django superuser yaratishda so'raladigan maydon
