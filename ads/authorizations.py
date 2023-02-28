from rest_framework.permissions import BasePermission


class IsSelectionOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsAdOwnerOrStaff(BasePermission):
    def has_object_permission(self, request, view, obj):
        if obj.author == request.user:
            return True
        return False

    def has_permission(self, request, view):
        if request.user.role in ["admin", "moderator"]:
            return True
        return False