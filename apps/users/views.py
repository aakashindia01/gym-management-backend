# from django.http import HttpResponse

# from .models import User
# from .serializers import CustomUserSerializer
# from rest_framework.views import APIView, Response, status

# class CustomUserView(APIView):
#     def post(self, request):
#         serializer = CustomUserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

#     def get(self, request, pk=None):
#         if pk is not None:
#             try:
#                 user = CustomUser.objects.get(id=pk)
#             except CustomUser.DoesNotExist:
#                 return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
#             serializer = CustomUserSerializer(user)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             users = CustomUser.objects.all()
#             serializer = CustomUserSerializer(users, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk):
#         user = CustomUser.objects.get(id=pk)
#         serializer = CustomUserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)