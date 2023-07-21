from rest_framework  import serializers
from .models import Answer,Question


class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()




class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Question
        fields = '__all__' 




class AnswerSerializer(serializers.Serializer):
    class Meta:
        model = Answer
        fields = '__all__'