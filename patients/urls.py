from django.urls import path, include
from rest_framework import routers
from patients import views

router = routers.DefaultRouter()

router.register('submit', views.PatientView, basename='submit')
