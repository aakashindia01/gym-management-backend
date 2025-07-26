from rest_framework import serializers
from .models import Tenant
from apps.users.models import User
from common.enums import Role, Status
from uuid import uuid4
from django.contrib.auth.hashers import make_password
import random
import string

class TenantAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'name', 'phone', 'currency', 'location', 'address', 'profilePicture']

    def create(self, validated_data):
        validated_data['role'] = Role.TENANT_ADMIN
        validated_data['status'] = Status.ACTIVE
        return User.objects.create(**validated_data)

class TenantOnboardSerializer(serializers.ModelSerializer):
    admin = TenantAdminSerializer()

    class Meta:
        model = Tenant
        fields = [
            'tenantId', 'tenantName', 'admin', 'email', 'phone', 'status',
            'profilePicture', 'address', 'gstId', 'currency'
        ]
        extra_kwargs = {
            'tenantId': {'read_only': True}
        }

    def create(self, validated_data):
        admin_data = validated_data.pop('admin')

        # Generate random password
        random_password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # Create the admin user first
        admin_user = User.objects.create(
            email=admin_data['email'],
            password=make_password(random_password),
            isTempPasswordReset=True,
            name=admin_data.get('name'),
            phone=admin_data.get('phone'),
            currency=admin_data.get('currency'),
            location=admin_data.get('location'),
            address=admin_data.get('address'),
            profilePicture=admin_data.get('profilePicture'),
            role=Role.TENANT_ADMIN,
            status=Status.ACTIVE,
        )

        tenant = Tenant.objects.create(
            tenantId=str(uuid4()),
            tenantName=validated_data.get('tenantName'),
            admin=admin_user,
            email=validated_data.get('email'),
            phone=validated_data.get('phone'),
            status=validated_data.get('status'),
            profilePicture=validated_data.get('profilePicture'),
            address=validated_data.get('address'),
            gstId=validated_data.get('gstId'),
            currency=validated_data.get('currency'),
        )

        # Update the user's tenantId and tenantOwnerId
        admin_user.tenantRef = tenant
        admin_user.tenantId = str(tenant.tenantId)
        admin_user.save()
        
        self._admin_password = random_password

        return tenant
    
    def get_admin_password(self):
        return getattr(self, '_admin_password', None)