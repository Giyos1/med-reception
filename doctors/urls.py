from django.urls import path
from .views import AdminDoctorCreateView

urlpatterns = [
    path('admin/doctors/', AdminDoctorCreateView.as_view(), name='admin-doctor-create'),
]