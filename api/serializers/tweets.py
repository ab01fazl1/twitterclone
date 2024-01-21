from rest_framework import serializers
from apps.tweet.models import Tweet

# from apps.tweet.services import get_retweet_count
from .users import UserSerializer


class TweetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["user", "text", "created_at"]


class GetTweetSerializer(serializers.ModelSerializer):

    replies = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    retweet_count = serializers.SerializerMethodField()
    reply_count = serializers.SerializerMethodField()

    user = UserSerializer()

    class Meta:
        model = Tweet
        fields = [
            "id",
            "user",
            "text",
            "created_at",
            "like_count",
            "retweet_count",
            "reply_count",
            "replies",
        ]

    def get_replies(self, obj: Tweet):
        return obj.children.filter(type=Tweet.TweetType.REPLY)

    def get_like_count(self, obj: Tweet):
        return obj.likes.count()

    def get_retweet_count(self, obj):
        return obj.children.filter(type=Tweet.TweetType.RETWEET).count()

    def get_reply_count(self, obj):
        return obj.children.filter(type=Tweet.TweetType.REPLY).count()


class ReplyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["user", "text", "created_at", "parent_tweet"]


class QuoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["user", "text", "created_at", "parent_tweet"]


class RetweetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ["user", "text", "created_at", "parent_tweet"]
