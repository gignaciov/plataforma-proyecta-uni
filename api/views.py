from django.contrib.auth.models import User
from rest_framework import generics, permissions

from django.shortcuts import render
from .models import Proyectino
from .serializers import ProyectinoSerializer,UserSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)

class UserList(generics.ListAPIView):
    """ View to list all users"""
    queryset = User.objects.all().order_by('first_name')
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class ProyectinoListCreate(generics.ListCreateAPIView):
    queryset = Proyectino.objects.all()
    serializer_class = ProyectinoSerializer
    permission_classes = (permissions.IsAuthenticated, )