from rest_framework import permissions
from rest_framework.views import View, Request

class ItsAdm(permissions.BasePermission):
    def has_permission(self, req: Request, view: View) -> bool:
        return (
            req.method in permissions.SAFE_METHODS or
            (req.user.is_authenticated and req.user.is_employee)
        )
