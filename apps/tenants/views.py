from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.tenants.serializers import TenantOnboardSerializer
from apps.users.permissions import IsSuperAdmin
from rest_framework.permissions import IsAuthenticated

class TenantOnboardView(APIView):
    def post(self, request):
        permission_classes = [IsAuthenticated, IsSuperAdmin]
        
        serializer = TenantOnboardSerializer(data=request.data)
        if serializer.is_valid():
            tenant = serializer.save()
            return Response({
                "message": "Tenant onboarded successfully",
                "tenantId": tenant.tenantId,
                "tenantAdminEmail": request.data.admin("email"),
                "tenantAdminPassword": serializer.get_admin_password()  # One-time response
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
