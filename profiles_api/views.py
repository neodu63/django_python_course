from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from profiles_api import serializers


class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """"Returns a list of APIView features"""
        
        an_apiview = [
            'Uses HTTP methods as functions (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Creates a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        """Applies put method on view"""
        return Response({'message': 'Applies PUT method'})
    
    def patch(self, request):
        """Applies patch method on view"""
        return Response({'message': 'Applies PATCH method'})
    
    def delete(self, request):
        """Applies delete method on view"""
        return Response({'message': 'Applies DELETE method'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet"""
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """Return a Hello message"""

        a_viewset = [
            'Uses actions (list, create, retieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provides more functionality with less code',
        ]

        return Response({'message': "Hello!", 'a_viewset': a_viewset})

    def create(self, request):
        """Creates a hello message with our name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        """Performs retrieve"""
        return Response({'message': 'Performs retrieve like GET'})
    
    def update(self, request, pk=None):
        """Performs update"""
        return Response({'message': 'Performs update like PUT'})
    
    def partial_update(self, request, pk=None):
        """Performs partial update"""
        return Response({'message': 'Performs partial update like PATCH'})
    
    def destroy(self, request, pk=None):
        """Performs destroy"""
        return Response({'message': 'Performs destroy like DELETE'})
