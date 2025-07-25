from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import serializers
from django.contrib.auth import authenticate
from apps.users.models import User

class TokenSerializer(TokenObtainPairSerializer):
    username_field = 'email'
    def validate(self, attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        user = authenticate(email=email, password=password)

        if user is None:
            raise serializers.ValidationError("Invalid email or password")

        data = super().validate(attrs)
        data['user'] = {
            'name': user.name ,
            'user_id' : user.memberId,
            'email': user.email,
            'role': user.role,
            'status': user.status,
        }
        return data