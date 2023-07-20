from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import UserRegisterSerializer
from rest_framework import status

class UserRegister(APIView):
    def post(self, request):
        serialized_user_data = UserRegisterSerializer(data=request.POST)
        if serialized_user_data.is_valid():
           serialized_user_data.create(serialized_user_data.validated_data)
           return Response(serialized_user_data.data,status=status.HTTP_200_OK)               
        return Response(serialized_user_data.errors,status=status.HTTP_400_BAD_REQUEST)

            
