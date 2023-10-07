from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.MenuModel import Menu
from server.model.PlateModel import Plate
from server.serializers.MenuSerializer import MenuSerializer
from server.serializers.PlateSerializer import PlateSerializer

class getMenus(APIView):
    def get(self, request,restaurant_id):
        menus = Menu.objects.filter(restaurant_id=restaurant_id)
        serializer = MenuSerializer(menus,many=True)
        return Response(serializer.data)
    
class getMenuIsPublished(APIView):
    def get(self, request,restaurant_id):
        menu = Menu.objects.filter(restaurant_id=restaurant_id,is_published=True).first()
        if menu is None:
            return Response({"message": "Not foud menu published"}, status=404)
        
        plates = Plate.objects.filter(restaurant_id=restaurant_id,menu_id=menu.id) #Search plates
        serializer_plate = PlateSerializer(plates,many=True)
        serializer_menu = MenuSerializer(menu)
        return Response({"menu":serializer_menu.data,"plates":serializer_plate.data})
    