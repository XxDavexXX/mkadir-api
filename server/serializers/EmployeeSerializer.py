from rest_framework import serializers
from server.model.EmployeeModel import Employee
from server.serializers.RoleSerializer import RoleSerializer
from server.serializers.UserSerializer import UserSerializer
class EmployeeSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    role = RoleSerializer()
    class Meta:
        model = Employee
        fields = ['id','user','restaurant','role','dni','address','age','phone','created_at','updated_at']    
        
        