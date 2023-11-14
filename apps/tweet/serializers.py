from rest_framework import serializers
from user.serializers import UserSerializer
from .models import Tweet, Reply, Quote


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['user', 'text', 'created_at']

    user = UserSerializer()


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['user', 'text', 'created_at', 'reply_to_tweet']

    user = UserSerializer()


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['user', 'text', 'created_at', 'quote_to_tweet']

    user = UserSerializer()
