from django.shortcuts import render
from rest_framework import viewsets
from .models import Like
from .serializers import LikeSerializer

class LikeView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
