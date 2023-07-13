from rest_framework.permissions import IsAuthenticated


class APIPermission(IsAuthenticated):
    def has_permission(self, request, view):
        return request.user.is_active
