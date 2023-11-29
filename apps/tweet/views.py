from django.shortcuts import render
from rest_framework.views import APIView
from .models import Tweet, Reply, Quote
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from rest_framework import status
from .serializers import TweetSerializer, ReplySerializer, QuoteSerializer, TweetUserSerializer
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import get_view_description
from rest_framework.decorators import api_view
from .query import users_tweets


class TweetView(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin, GenericViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetUserViewSet(RetrieveModelMixin, ListModelMixin, GenericViewSet):
    serializer_class = TweetSerializer

    def get_queryset(self):
        return Tweet.objects.filter(user=self.kwargs['users_pk'])

    def get_serializer_context(self):
        return {"user": self.kwargs['users_pk']}


class ReplyView(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class QuoteView(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer
