from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class IndexApiView(APIView):
    def get(self, request):
        try:
            response_data = {'message': 'Successfully'}
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            # Si ocurre un error
            error_message = 'Error occurred: {}'.format(str(e))
            return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)
