from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied


class IsOwnerOrAdmin(permissions.BasePermission):
    """Проверка авторизации и доступа к объектам."""

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if obj.user == request.user or request.user.is_staff:
            return True
        raise PermissionDenied('Вы не можете изменить или удалить этот пост,'
                               'так как он принадлежит другому пользователю.')
