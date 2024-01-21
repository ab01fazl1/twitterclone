from django.shortcuts import render
from rest_framework.generics import CreateAPIView, DestroyAPIView
from apps.like.models import Like
from api.serializers.like import LikeSerializer


class LikeViewSet(CreateAPIView, DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
