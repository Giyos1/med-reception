from django.contrib.auth.models import AbstractUser
from rest_framework_simplejwt import models
from django.db import models


class User(AbstractUser):
    pass


class PatientApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    condition = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'patient_application'
