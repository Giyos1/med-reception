from django.urls import path
from patients.views import PatientListView
from doctors.views import DoctorCreateView

urlpatterns = [
    # ... mavjud url'lar
    path('api/admin/patients/', PatientListView.as_view()),
    path('api/admin/doctors/', DoctorCreateView.as_view()),
]