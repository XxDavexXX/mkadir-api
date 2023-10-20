from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.RestaurantModel import Restaurant
from server.middlewares.AuthMiddleware import AuthRequired
from rest_framework.exceptions import AuthenticationFailed

# from server.model.MenuModel import Menu
from server.serializers.RestaurantSerializer import RestaurantSerializer
class getAllRestaurants(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all().order_by('-is_open')
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)
    
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

