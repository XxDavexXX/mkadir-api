from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.RestaurantModel import Restaurant
from server.serializers.RestaurantSerializer import RestaurantSerializer
class getRestaurants(APIView):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurants, many=True)
        return Response(serializer.data)