from rest_framework import serializers
from .models import Tweet, Reply, Quote


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['user', 'text', 'created_at']

class TweetUserSerializer():
    pass
#     def create(self, validated_data):
#
#         return super().create(validated_data)
class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['user', 'text', 'created_at', 'reply_to_tweet']



class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['user', 'text', 'created_at', 'quote_to_tweet']

