from django.db import models
from accounts.models import User


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    specialization = models.CharField(max_length=200)
    procedure_cost = models.DecimalField(max_digits=10, decimal_places=2)