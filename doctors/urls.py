from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AdminDoctorViewSet

router = DefaultRouter()
router.register(r'', AdminDoctorViewSet, basename='admin-doctor')

urlpatterns = [
    path('', include(router.urls)),
]