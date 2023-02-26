from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAutherOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(
            # get access to super user
            # request.user.is_authenticated and request.user.is_superuser or
            # get access to auther of object
            request.user.is_authenticated and obj.auther == request.user

        )


class IsSuperUser(BaseException):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
