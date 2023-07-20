from rest_framework.views import APIView 
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import UserRegisterSerializer

class UserRegister(APIView):
    def post(self, request):
        user_serializer_data = UserRegisterSerializer(data=request.POST)
        if user_serializer_data.is_valid():
            User.objects.create_user(
                username = user_serializer_data.validated_data['username'],
                email = user_serializer_data.validated_data['email'],
                password = user_serializer_data.validated_data['password']
            )
            return Response(user_serializer_data.data)               
        return Response(user_serializer_data.errors)

            
