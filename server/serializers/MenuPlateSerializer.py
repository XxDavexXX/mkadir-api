from rest_framework import serializers
from server.model.MenuPlateModel import MenuPlate


# Related models serializer
from server.serializers.PlateSerializer import PlateSerializer
from server.serializers.RestaurantSerializer import RestaurantSerializer
from server.serializers.MenuSerializer import MenuSerializer 

class MenuPlateSerializer(serializers.ModelSerializer):
    menu = MenuSerializer()
    plate = PlateSerializer()
    restaurant = RestaurantSerializer()
    class Meta:
        model = MenuPlate
        fields = ['id','plate','restaurant','menu']    


