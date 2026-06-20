from django.contrib import admin
from django.urls import path,include
from users.views import LoginView, LogoutView, CustomTokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls')),
    path('api/auth/login/', LoginView.as_view(), name='auth_login'),
    path('api/auth/logout/', LogoutView.as_view(), name='auth_logout'),
    path('api/auth/token/refresh/', CustomTokenRefreshView.as_view(), name='auth_token_refresh'),
]
