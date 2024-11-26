from rest_framework.permissions import BasePermission, AllowAny


class IsOwner(BasePermission):
    """
    Проверка пользователя к принадлежности создания привычки
    """
    def has_object_permission(self, request, view, object):
        if object.user == request.user:
            return True
        return False




