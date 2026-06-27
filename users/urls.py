from django.urls import path
from rest_framework import routers
from patients.views import PatientView
from users.views import LoginView, LogoutView, CustomTokenRefreshView

urlpatterns = [
    path('login/', LoginView.as_view(), name='auth_login'),
    path('logout/', LogoutView.as_view(), name='auth_logout'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='auth_token_refresh'),
]
