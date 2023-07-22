from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person,Question,Answer
from .serializers import PersonSerializer,QuestionSerializer,AnswerSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser

class Home(APIView):

    permission_classes = [IsAdminUser,]

    def get(self,request):
        person = Person.objects.all()    
        srz_data = PersonSerializer(instance= person,many= True)                   
        return Response(data = srz_data.data,status=status.HTTP_200_OK)




class QuestionView(APIView):

    def get(self,request):
        #question =  Question.objects.all()
        srz_data = QuestionSerializer(instance= Question.objects.all(), many =True)
        return Response(data = srz_data.data,status=status.HTTP_200_OK)

    def post(self,request):
        pass


    def put(self,request,pk):
        pass


    def delete(self,request,pk):
        pass
    
    