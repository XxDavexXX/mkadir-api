from rest_framework import serializers
from server.model.UserModel import User
# Esto es para convertir los datos a formato JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'name', 'paternal_surname', 'maternal_surname', 'dni', 'picture', 'username']
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True, 'error_messages': {'required': 'This field is required.'}},
            # Add extra_kwargs for other fields if needed
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class RegisterSerializer(UserSerializer):
    # You can add any additional validation or fields specific to registration if needed
    pass

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, error_messages={'required': 'This field is required.'})
    password = serializers.CharField(required=True, error_messages={'required': 'This field is required.'})