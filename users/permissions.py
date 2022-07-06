from rest_framework import permissions


class IsUser(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return request.user.id == obj.id

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser