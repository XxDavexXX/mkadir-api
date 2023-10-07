from rest_framework import serializers
from server.model.CategoryPlateModel import CategoryPlate
class PlateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryPlate
        fields = ['id','name','description']    