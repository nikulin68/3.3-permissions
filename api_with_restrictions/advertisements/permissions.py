from rest_framework.permissions import BasePermission


class IsOwnerOrReadOnlyOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'GET' or request.user.is_superuser:
            return True
        return request.user == obj.creator
