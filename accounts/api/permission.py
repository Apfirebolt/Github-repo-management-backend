from rest_framework import permissions
from . exceptions import UnauthorizedException


class IsUserAuthenticated(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        else:
            raise UnauthorizedException