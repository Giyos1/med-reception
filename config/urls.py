from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Swagger uchun asosiy ma'lumotlar konfiguratsiyasi
schema_view = get_schema_view(
   openapi.Info(
      title="Med Reception API",
      default_version='v1',
      description="Qabulxona va shifokorlar tizimi API hujjatlari",
      contact=openapi.Contact(email="support@medreception.uz"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny,],
)

# 3-qism: Konfiguratsiya. Api prefixi bor endpointlarni birlashtirish
api_v1_patterns = [
    path('accounts/', include('users.urls')),
    path('api/doctors/', include('doctors.urls')),
    # path('patients/', include('patients.urls'))
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(api_v1_patterns)), # birlashtirildi
    # 2-qism: drf-yasg orqali Swagger va ReDoc URL-lari
    path('api/docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
