from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        # authenticate() ichida username=email beramiz, chunki USERNAME_FIELD='email'
        user = authenticate(username=data['email'], password=data['password'])
        if not user:
            raise serializers.ValidationError('Email yoki parol noto\'g\'ri.')
        if not user.is_active:
            raise serializers.ValidationError('Foydalanuvchi faol emas.')
        data['user'] = user
        return data


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """
    POST /api/login/
    Tizimga kirish — Token qaytaradi.
    """
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    token, _ = Token.objects.get_or_create(user=user)
    return Response({
        'token': token.key,
        'user_id': user.pk,
        'email': user.email,
        'role': user.role,
        'full_name': user.get_full_name(),
    })