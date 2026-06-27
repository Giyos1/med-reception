from patients.models import Patient
from rest_framework import serializers



class PatientSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields ="__all__"
