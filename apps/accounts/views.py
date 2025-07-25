from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import TokenSerializer

class TokenSerializer(TokenObtainPairView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return response
