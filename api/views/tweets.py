from rest_framework.response import Response

from rest_framework import status
from api.serializers.tweets import (
    RetweetCreateSerializer,
    TweetCreateSerializer,
    ReplyCreateSerializer,
    GetTweetSerializer,
    QuoteCreateSerializer,
)
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import RetrieveModelMixin
from apps.tweet.models import Tweet
from apps.tweet.services import create_tweet, create_reply, create_quote, create_retweet


class CreateTweetView(GenericAPIView):
    serializer_class = TweetCreateSerializer
    # permission_classes

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        create_tweet(user=self.request.user, text=serializer.validated_data["text"])
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class GetTweetView(GenericAPIView, RetrieveModelMixin):
    queryset = Tweet.objects.all()
    serializer_class = GetTweetSerializer
    # pagination class

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class CreateReplyView(GenericAPIView):

    serializer_class = ReplyCreateSerializer
    # permission_classes

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]
        parent_tweet = serializer.validated_data["parent_tweet_pk"]

        create_reply(user=self.request.user, text=text, parent_tweet=parent_tweet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateQuoteView(GenericAPIView):

    serializer_class = QuoteCreateSerializer
    # permission_classes

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        text = serializer.validated_data["text"]
        parent_tweet = serializer.validated_data["parent_tweet_pk"]

        create_quote(user=self.request.user, text=text, parent_tweet=parent_tweet)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CreateRetweetView(GenericAPIView):
    serializer_class = RetweetCreateSerializer
