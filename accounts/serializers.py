from rest_framework import serializers


def clean_admin(value):
     if 'admin' in value:
         raise serializers.ValidationError(f'`{value}` CAN NOT CONTAIN `admin`')

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(required = True,validators=[clean_admin])
    email = serializers.EmailField(required = True,validators=[clean_admin])
    password = serializers.CharField(required = True, write_only = True)
    passwordConfirm = serializers.CharField(required = True, write_only = True)

    def validate(self,data):
        if data['password'] != data['passwordConfirm']:
            raise serializers.ValidationError('password ARE NOT SAME')
        return data
    

    

    