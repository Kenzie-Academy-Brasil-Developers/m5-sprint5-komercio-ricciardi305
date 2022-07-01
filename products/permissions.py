from rest_framework import permissions

class FreeGetPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        
        if request.user.is_authenticated and request.user.is_seller:
            return True
        
        return False
        
class IsSellerOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == "GET":
            return True
        if request.user.is_authenticated and request.user.is_seller:
            return obj.seller == request.user
        return False