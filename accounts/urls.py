from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenBlacklistView,
)
from accounts.views import PatientRegisterView

# router = DefaultRouter()
# router.register('patient-register', PatientRegisterView)
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
    path('api/token/blacklist/', TokenBlacklistView.as_view()),
    path('api/register/', PatientRegisterView.as_view(), name='patient-register')
]
