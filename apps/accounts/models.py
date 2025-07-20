from django.db import models
from rest_framework import generics, permissions
from apps.users.models import User
from apps.users.serializers import RegisterSerializer
from apps.users.permissions import IsSuperAdmin, IsTenantAdmin
from common.enums import Role

class SuperAdminRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]

    def perform_create(self, serializer):
        serializer.save(role=Role.SUPER_ADMIN, addedBy=self.request.user.email)

class TenantAdminRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]
    addedBy = None

    def perform_create(self, serializer):
        serializer.save(role=Role.TENANT_ADMIN, addedBy=None)

class StaffRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save(role='staff', tenantId=self.request.user.tenantId, addedBy=self.request.user.email)


class MemberRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsTenantAdmin]

    def perform_create(self, serializer):
        serializer.save(role='member', tenantId=self.request.user.tenantId, addedBy=self.request.user.email)
