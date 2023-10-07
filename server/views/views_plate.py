from rest_framework.views import APIView
from rest_framework.response import Response
from server.model.PlateModel import Plate
from server.serializers.PlateSerializer import PlateSerializer
class getPlates(APIView):
    def get(self, request, restaurant_id):
        plates = Plate.objects.filter(restaurant_id=restaurant_id)
        serializer = PlateSerializer(plates,many=True)
        return Response(serializer.data)        