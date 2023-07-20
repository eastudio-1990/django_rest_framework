from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import UserRegisterSerializer

class UserRegister(APIView):
    def post(self, request):
        serialized_user_data = UserRegisterSerializer(data=request.POST)
        if serialized_user_data.is_valid():
           serialized_user_data.create(serialized_user_data.validated_data)
           return Response(serialized_user_data.data)               
        return Response(serialized_user_data.errors)

            
