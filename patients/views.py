from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from patients.models import Patient
from patients.serialazer import PatientSubmitSerializer


class PatientView(APIView):
    serializer_class=PatientSubmitSerializer
    queryset=Patient.objects.all()
    permission_classes=(AllowAny,)