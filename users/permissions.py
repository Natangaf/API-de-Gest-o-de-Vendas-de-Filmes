from rest_framework import permissions
from rest_framework.views import View, Request


class UserAccessPermission(permissions.BasePermission):
    def has_permission(self, req: Request, view: View) -> bool:
        return req.method in permissions.SAFE_METHODS or (
            req.user.is_authenticated and req.user.is_employee
        )
    
class itsUser(permissions.BasePermission):
    def has_object_permission(self, req, view, obj):
        return obj == req.user or req.user.is_employee
