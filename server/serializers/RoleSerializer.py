from rest_framework import serializers
from server.model.RoleModel import Role

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = ['id','name','description','created_at','updated_at']    