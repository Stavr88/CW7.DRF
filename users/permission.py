from rest_framework.permissions import BasePermission, AllowAny


class IsModerator(BasePermission):
    """
    Проверка пользователя к принадлежности
    """

    def has_permission(self, request, view):
        return request.user.groups.filter(name="moderators").exists()


class IsOwner(BasePermission):
    """
    Проверка пользователя к принадлежности создания привычки
    """
    def has_object_permission(self, request, view, object):
        if object.owner == request.user:
            return True
        return False




