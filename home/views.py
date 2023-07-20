from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer
from rest_framework import status

class Home(APIView):
    def get(self,request):
        person = Person.objects.all()    
        serialized_person_data = PersonSerializer(instance= person,many= True)                   
        return Response(data = serialized_person_data.data,status=status.HTTP_200_OK)

