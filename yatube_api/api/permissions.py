from rest_framework import permissions


class IsAutorOrReadOnly(permissions.BasePermission):
    message = 'Изменение чужого контента запрещено!'

    def has_object_permission(self, request, obj):
        return (request.method in permissions.SAFE_METHODS
                or obj.author == request.user)
