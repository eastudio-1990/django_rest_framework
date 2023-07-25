from rest_framework  import serializers
from .models import Answer,Question
from .custome_relational_fields import UserEmailUserNameRelationalField

class PersonSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    email = serializers.EmailField()




class QuestionSerializer(serializers.ModelSerializer):
     
     answers = serializers.SerializerMethodField()
     #user = serializers.SlugRelatedField(read_only = True,slug_field= 'email')  
     user = UserEmailUserNameRelationalField(read_only= True)

     class Meta:
         model = Question
         fields = '__all__'

     def get_answers(self,obj):
         result = obj.answers.all()
         return AnswerSerializer(instance=result, many= True).data   




class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'