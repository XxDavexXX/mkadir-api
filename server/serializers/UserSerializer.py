from rest_framework import serializers
from server.model.UserModel import User
# Esto es para convertir los datos a formato JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','password','name','paternal_surname','maternal_surname','dni','picture','username']
        extra_kwargs = {
            'password': {'write_only': True}
        }
    
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance