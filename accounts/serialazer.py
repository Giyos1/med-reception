from rest_framework import serializers
from django.db import models

from accounts.models import PatientApplication


class PatientApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatientApplication
        fields = ['first_name', 'last_name', 'phone_number','condition']
