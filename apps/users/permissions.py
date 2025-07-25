from rest_framework.permissions import BasePermission
from common.enums import Role

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.SUPER_ADMIN

class IsTenantAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == Role.TENANT_ADMIN
