from rest_framework import serializers
from server.model.PlateModel import Plate
from server.serializers.CategoryPlateSerializer import PlateSerializer
class PlateSerializer(serializers.ModelSerializer):
    category = PlateSerializer()
    class Meta:
        model = Plate
        fields = ['id','img_url','name','description','price','category','restaurant']    