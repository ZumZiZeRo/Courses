from django.http import response
from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self, request, format=None):
        """Returns a list of APIViews Features"""
        an_apiview = [
            'Uses HTTP methods as function (get,post,patch,put,delete)',
            'is similar to a traditional Django View',
            'gives you the most control over you application logic',
            'is mapped manually to urls'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})
