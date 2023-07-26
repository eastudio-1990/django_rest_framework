from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Person,Question,Answer
from .serializers import PersonSerializer,QuestionSerializer,AnswerSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated,IsAdminUser
from permissions import IsOwnerOrReadOnly

class Home(APIView):

    permission_classes = [IsAuthenticated,]

    def get(self,request):
        person = Person.objects.all()    
        srz_data = PersonSerializer(instance= person,many= True)                   
        return Response(data = srz_data.data,status=status.HTTP_200_OK)




class QuestionListView(APIView):

    def get(self,request):
        srz_data = QuestionSerializer(instance= Question.objects.all(), many =True)
        return Response(data = srz_data.data,status=status.HTTP_200_OK)

class QuestionCreateView(APIView):
    
    permission_classes = [IsAuthenticated,]
    serializer_class = QuestionSerializer

    def post(self,request):
        srz_data = QuestionSerializer(data= request.data)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_201_CREATED)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)


class QuestionUpdateView(APIView):

    permission_classes = [IsOwnerOrReadOnly,]
    serializer_class = QuestionSerializer

    def put(self,request,pk):
        question = Question.objects.get(pk=pk)
        self.check_object_permissions(request,question)
        srz_data = QuestionSerializer(instance=question, data=request.data, partial = True)
        if srz_data.is_valid():
            srz_data.save()
            return Response(srz_data.data,status=status.HTTP_200_OK)
        return Response(srz_data.errors,status=status.HTTP_400_BAD_REQUEST)

class QuestionDeleteView(APIView):

    permission_classes = [IsOwnerOrReadOnly,]
    
    def delete(self,request,pk):
        question = Question.objects.get(pk=pk)
        question.delete()
        return Response(status=status.HTTP_200_OK)
    
