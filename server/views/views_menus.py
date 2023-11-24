from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.MenuModel import Menu
from server.model.PlateModel import Plate
from server.serializers.MenuSerializer import MenuSerializer
from server.serializers.PlateSerializer import PlateSerializer
from server.middlewares.AuthMiddleware import AuthRequired
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import ValidationError
class getMenus(APIView):
    def get(self, request,restaurant_id):
        menus = Menu.objects.filter(restaurant_id=restaurant_id)
        serializer = MenuSerializer(menus,many=True)
        return Response(serializer.data)

class getMenu(APIView):
    def get(self,request,menu_id,restaurant_id):
        try:
            menu = Menu.objects.get(id=menu_id,restaurant_id=restaurant_id)
        except Menu.DoesNotExist:
            return Response({'message': 'Menu not found'}, status=404)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)

class deleteMenu(APIView):
    def delete(self,request,menu_id,restaurant_id):
        try:
            AuthRequired(request)  
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401) 
        try:
            menu = Menu.objects.get(id=menu_id, restaurant_id=restaurant_id)
        except Menu.DoesNotExist:
            return Response({'message': 'Menu not found'}, status=404) 
        menu.delete()
        return Response({'message': 'Menu deleted successfully'}, status=200)
class createMenu(APIView):
    def post(self,request,restaurant_id):
        try:
            user = AuthRequired(request) 
            request.data['user'] = user['id'] 
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401) 
        
        request.data['restaurant']  = restaurant_id 
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class updateMenu(APIView):
   def put(self, request, restaurant_id,menu_id):
        print(restaurant_id)
        try:
            AuthRequired(request)
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401)
        try:
            menu = Menu.objects.get(id=menu_id,restaurant_id=restaurant_id)
        except Menu.DoesNotExist:
            return Response({'message': 'Menu not found'}, status=404)
        
        serializer = MenuSerializer(menu, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class getMenusIsPublished(APIView):
    def get(self, request,restaurant_id):
        menu = Menu.objects.filter(restaurant_id=restaurant_id,is_published=True)
        serializer = MenuSerializer(menu,many=True)
        return Response(serializer.data)
    
class getMenuIsPublished(APIView):
    def get(self, request,restaurant_id):
        menu = Menu.objects.filter(restaurant_id=restaurant_id,is_published=True).first()
        print(menu.is_published)
        if menu is None:
            return Response({"message": "Not foud menu published"}, status=404)
        
        plates = Plate.objects.filter(restaurant_id=restaurant_id,menu_id=menu.id) #Search plates
        serializer_plate = PlateSerializer(plates,many=True)    
        serializer_menu = MenuSerializer(menu)
        return Response({"menu":serializer_menu.data,"plates":serializer_plate.data})
    