from django.shortcuts import render
from rest_framework.views import APIView
from .models import Tweet, Reply, Quote
from rest_framework.response import Response
from rest_framework import generics
from django.http import Http404
from rest_framework import status
from .serializers import TweetSerializer, ReplySerializer, QuoteSerializer


class TweetView(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    def get_object(self, username, pk):
        try:
            return Tweet.objects.get(user__iexact=username, pk=pk)
        except Tweet.DoesNotExist:
            raise Http404

    serializer_class = TweetSerializer


class ReplyView(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer


class QuoteView(generics.RetrieveDestroyAPIView, generics.CreateAPIView):
    queryset = Quote.objects.all()
    serializer_class = QuoteSerializer



