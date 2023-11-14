from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.generics import CreateAPIView
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

class CreateUserView(CreateAPIView):

    model = User.objects.all()
    # permission_classes = [
    #     permissions.AllowAny # Or anon users can't register
    # ]
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
