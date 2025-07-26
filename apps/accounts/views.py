from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenSerializer
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
    permission_classes = [permissions.IsAuthenticated, IsSuperAdmin]
    addedBy = None

    def perform_create(self, serializer):
        serializer.save(role=Role.TENANT_ADMIN, addedBy=None)

class StaffRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsTenantAdmin]

    def perform_create(self, serializer):
        serializer.save(role=Role.STAFF, tenantId=self.request.user.tenantId, addedBy=self.request.user.email)

class ManagerRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsTenantAdmin]

    def perform_create(self, serializer):
        serializer.save(role=Role.MANAGER, tenantId=self.request.user.tenantId, addedBy=self.request.user.email)

class MemberRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsTenantAdmin]

    def perform_create(self, serializer):
        serializer.save(role=Role.MEMBER, tenantId=self.request.user.tenantId, addedBy=self.request.user.email)



class TokenSerializer(TokenObtainPairView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
