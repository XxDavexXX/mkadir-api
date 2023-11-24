
from rest_framework.views import APIView
from rest_framework.response import Response
from server.serializers.RoleSerializer import RoleSerializer
from server.model.RoleModel import Role
class getRoles(APIView):
    def get(self, request):
        roles = Role.objects.filter()
        serializer = RoleSerializer(roles,many=True)
        return Response(serializer.data)        
