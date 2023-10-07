from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.MenuPlateModel import MenuPlate
from server.serializers.MenuPlateSerializer import MenuPlateSerializer

class getMenusPlates(APIView):
    def get(self, request,restaurant_id):
        menus = MenuPlate.objects.filter(restaurant_id=restaurant_id)
        serializer = MenuPlateSerializer(menus,many=True)
        return Response(serializer.data)
    

