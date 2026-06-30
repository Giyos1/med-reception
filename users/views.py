from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import CustomTokenObtainPairSerializer

# 2 qism: barcha endpointlar(im) uchun schema yozish
# 1. LOGIN SCHEMA
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Tizimga kirish (Login)",
        operation_description="Telefon raqam va parol orqali JWT tokenlar hamda foydalanuvchi rolini olish.",
        responses={
            200: openapi.Response(
                description="Muvaffaqiyatli kirish",
                examples={
                    "application/json": {
                        "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpX...",
                        "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpX...",
                        "role": "shifokor"
                    }
                }
            ),
            400: "Telefon raqam yoki parol xato."
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# 2. REFRESH TOKEN SCHEMA
class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        operation_summary="Tokenni yangilash (Refresh)",
        operation_description="Eski refresh tokenni yuborib, yangi access va refresh tokenlarni olish.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['refresh'],
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING, description="Amaldagi refresh token")
            },
        ),
        responses={
            200: openapi.Response(
                description="Yangi tokenlar berildi",
                examples={
                    "application/json": {
                        "access": "yangi_access_token_shu_yerda",
                        "refresh": "yangi_refresh_token_shu_yerda"
                    }
                }
            ),
            401: "Token yaroqsiz yoki muddati o'tgan"
        }
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


# LOGOUT SCHEMA
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        operation_summary="Tizimdan chiqish (Logout)",
        operation_description="Amaldagi refresh tokenni qora ro'yxatga (Blacklist) qo'shish va tizimdan chiqish.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            required=['refresh'],
            properties={
                'refresh': openapi.Schema(type=openapi.TYPE_STRING,
                                          description="Blacklist qilinishi kerak bo'lgan refresh token")
            },
        ),
        responses={
            200: openapi.Response(
                description="Tizimdan muvaffaqiyatli chiqildi",
                examples={
                    "application/json": {
                        "message": "Tizimdan muvaffaqiyatli chiqildi (Token blacklist qilindi)."
                    }
                }
            ),
            400: "Yaroqsiz token yoki token allaqachon blacklist qilingan.",
            401: "Bearer token yuborilmagan yoki xato."
        }
    )
    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token majburiy"}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response({"message": "Tizimdan muvaffaqiyatli chiqildi (Token blacklist qilindi)."},
                            status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": "Yaroqsiz token yoki token allaqachon blacklist qilingan."},
                            status=status.HTTP_400_BAD_REQUEST)
