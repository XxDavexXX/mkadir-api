from rest_framework import serializers
from server.model.RestaurantModel import Restaurant
from server.serializers.UserSerializer import UserSerializer
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant  
        fields = ['id','logo_url','name','address','user']    
