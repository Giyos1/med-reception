from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework import mixins
from patients.models import Patient
from patients.serialazer import PatientSubmitSerializer


class PatientView(mixins.CreateModelMixin, GenericAPIView):
    serializer_class = PatientSubmitSerializer
    queryset = Patient.objects.all()
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
