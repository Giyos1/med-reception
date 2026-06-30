# reception/permissions.py
from rest_framework.permissions import BasePermission

class IsDoctor(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and
            request.user.is_authenticated and
            getattr(request.user, 'role', None) == 'shifokor'
        )

class IsAdminOrDoctor(BasePermission):
    def has_permission(self, request, view):
        if not (request.user and request.user.is_authenticated):
            return False

        user_role = getattr(request.user, 'role', None)
        return user_role in ['admin', 'shifokor']

