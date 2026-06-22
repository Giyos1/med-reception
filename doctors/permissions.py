from rest_framework.permissions import BasePermission


class IsAdministrator(BasePermission):
    message = "Sizda administrator huquqi yo'q."

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == 'admin'
        )