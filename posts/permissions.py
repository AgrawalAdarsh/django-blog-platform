from rest_framework.permissions import BasePermission

class IsWriterOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['writer','admin']

class IsOwnerOrAdmin(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user or request.user.role == 'admin'
