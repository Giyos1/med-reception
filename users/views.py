from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import CustomTokenObtainPairSerializer


# 1. Login View (Custom serializer bilan)
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]


# 2. Refresh Token View (Standart)
class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]


# 3. Logout View (Tokenni Blacklistga qo'shish)
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token majburiy"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # Tokenni blacklistga kiritish

            return Response({"message": "Tizimdan muvaffaqiyatli chiqildi (Token blacklist qilindi)."},
                            status=status.HTTP_200_OK)
        except:
            return Response({"error": "Yaroqsiz token yoki token allaqachon blacklistga kiritilgan."},
                            status=status.HTTP_400_BAD_REQUEST)
