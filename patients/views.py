from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from patients.models import Patient
from patients.serialazer import PatientSubmitSerializer


class PatientView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = PatientSubmitSerializer
    queryset = Patient.objects.all()
    permission_classes = (AllowAny,)
