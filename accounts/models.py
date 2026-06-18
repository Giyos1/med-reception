from django.contrib.auth.models import AbstractUser
from rest_framework.views import APIView
from rest_framework_simplejwt import models
from rest_framework_simplejwt.tokens import RefreshToken


class User(AbstractUser):
    @property
    def token(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

    class Meta:
        db_table = 'user'
