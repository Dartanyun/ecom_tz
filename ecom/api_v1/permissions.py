from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Проверяет является ли запрос безопасным или является
    ли автор запроса суперпользователем. В случае прохождения
    проверки отправляет True, иначе False.
    """

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.method in permissions.SAFE_METHODS
            or request.user.is_staff
        )
