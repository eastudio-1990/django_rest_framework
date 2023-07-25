from rest_framework.views import APIView 
from rest_framework.response import Response
from .serializers import UserRegisterSerializer,UserSerializer
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404



class UserRegister(APIView):
    def post(self, request):
        serialized_user_data = UserRegisterSerializer(data=request.POST)
        if serialized_user_data.is_valid():
           serialized_user_data.create(serialized_user_data.validated_data)
           return Response(serialized_user_data.data,status=status.HTTP_200_OK)               
        return Response(serialized_user_data.errors,status=status.HTTP_400_BAD_REQUEST)

            


class UserViewSet(viewsets.ViewSet):

    permission_classes = [IsAuthenticated,]
    user_queryset = User.objects.all()

    def list(self,request):
        srz_data = UserSerializer(instance= self.user_queryset,many= True)
        return Response(data=srz_data.data)

   
    def retrieve(self,request,pk = None):
        user = get_object_or_404(self.user_queryset,pk=pk)
        srz_data = UserSerializer(instance=user)
        return Response(data=srz_data.data)


    def partial_update(self,request,pk=None):       
        user = get_object_or_404(self.user_queryset, pk=pk)

        if user != request.user:
            return Response({'message' : 'you are not owner'})
        
        srz_data = UserSerializer(instance=user, data=request.POST, partial = True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(data=srz_data.data)
        return Response(data=srz_data.errors)
    
    def destroy(self,request,pk=None):                
        user = get_object_or_404(self.user_queryset,pk=pk)
        if user != request.user:
            return Response({'message' : 'you are not owner'})
        user.is_active = False
        user.save()
        return Response({'message':'user hase deActivated'})