from rest_framework import serializers
from django.contrib.auth.models import User

def clean_admin(value):
     if 'admin' in value:
         raise serializers.ValidationError(f'`{value}` CAN NOT CONTAIN `admin`')

class UserRegisterSerializer(serializers.ModelSerializer):

    passwordConfirm = serializers.CharField(required = True ,write_only = True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'passwordConfirm')

        extra_kwargs ={
                    
                    'password':{'write_only':True},
                       
                       'email':{'validators':(clean_admin,)},

                       'username':{'validators':(clean_admin,)}
                       
                       }
    def create(self, validated_data):
        del validated_data['passwordConfirm']
        return User.objects.create_user(**validated_data)


    # username = serializers.CharField(required = True,validators=[clean_admin])
    # email = serializers.EmailField(required = True,validators=[clean_admin])
    # password = serializers.CharField(required = True, write_only = True)
    # passwordConfirm = serializers.CharField(required = True, write_only = True)

    # def validate_username(self,value):
    #     if 'admin' in value:
    #         raise serializers.ValidationError('username CAN NOT CONTAIN `admin` name')
    #     return value


    def validate(self,data):
        if data['password'] != data['passwordConfirm']:
            raise serializers.ValidationError('password ARE NOT SAME')
        return data
    

    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
    