from rest_framework import serializers
from server.model.MenuModel import Menu
class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','img_menu_url','menu_name','description','is_published','created_at','updated_at','restaurant']    