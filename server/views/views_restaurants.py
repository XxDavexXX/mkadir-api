from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from server.model.RestaurantModel import Restaurant
from server.model.MenuModel import Menu
from server.middlewares.AuthMiddleware import AuthRequired
from rest_framework.exceptions import AuthenticationFailed

# from server.model.MenuModel import Menu
from server.serializers.RestaurantSerializer import RestaurantSerializer
from server.serializers.MenuSerializer import MenuSerializer

class getAllRestaurants(APIView):
    def get(self, request):
        page_number = request.query_params.get('page', 1)
        paginator = PageNumberPagination()
        paginator.page_size = 2
        restaurants = Restaurant.objects.all().order_by('-is_open')
        # Filtramos los restaurantes que tienen menús publicados
        restaurants_with_menus = []
        for restaurant in restaurants:
            if Menu.objects.filter(restaurant_id=restaurant.id, is_published=True).exists():
                restaurants_with_menus.append(restaurant)
        
        # Paginamos los resultados para la página solicitada
        paginated_restaurants = paginator.paginate_queryset(restaurants_with_menus, request)
        
        # Serializamos los restaurantes con sus menús
        serialized_data = []
        for restaurant in paginated_restaurants:
            restaurant_data = RestaurantSerializer(restaurant).data
            menu = Menu.objects.filter(restaurant_id=restaurant.id, is_published=True)
            menu_serializer = MenuSerializer(menu, many=True)
            restaurant_data['menus'] = menu_serializer.data
            serialized_data.append(restaurant_data)

        # Devolvemos los resultados paginados con los menús incluidos
        return paginator.get_paginated_response(serialized_data)
    
class registerRestaurant(APIView):
    def post(self, request):
        try:
            user = AuthRequired(request) 
            request.data['user'] = user['id'] 
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401) 
        
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class createRestaurant(APIView):
    def post(self, request):
        try:
            user = AuthRequired(request) 
            request.data['user'] = user['id'] 
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401) 
        
        serializer = RestaurantSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class getRestaurants(APIView):
    def get(self, request):
        try:
            user = AuthRequired(request)  
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401) 
        restaurants = Restaurant.objects.filter(user=user['id']).order_by('-is_open')
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)

class getRestaurant(APIView):
    def get(self, request,restaurant_id):
        try:
            user = AuthRequired(request)  
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401) 
        try:
            restaurant = Restaurant.objects.get(user=user['id'], id=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=404) 
        serializer = RestaurantSerializer(restaurant)
        return Response(serializer.data)
    
class deleteRestaurant(APIView):
    def delete(self, request,restaurant_id):
        try:
            user = AuthRequired(request)  
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401) 
        try:
            restaurant = Restaurant.objects.get(user=user['id'], id=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=404) 
        restaurant.delete()
        return Response({'message': 'Restaurant deleted successfully'}, status=200)

class updateRestaurant(APIView):
    def put(self, request, restaurant_id):
        try:
            user = AuthRequired(request)
        except AuthenticationFailed as e:
            return Response({'message': str(e)}, status=401)
        try:
            restaurant = Restaurant.objects.get(user=user['id'], id=restaurant_id)
        except Restaurant.DoesNotExist:
            return Response({'message': 'Restaurant not found'}, status=404)
        
        serializer = RestaurantSerializer(restaurant, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

