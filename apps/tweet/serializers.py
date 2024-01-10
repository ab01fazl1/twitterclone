from rest_framework import serializers
from .models import Tweet, Reply, Quote
from twitter.apps.Hashtag.models import Hashtag
import re


# this function finds the hashtags in the tweet_text and creates the new hashtag objects
# TODO: look into the possibility of moving this piece of code to the hashtag app itself
def process_hashtags(text, tweet):
    regex = "#(\w+)"
    hashtag_list = re.findall(regex, text)
    for hashtag in hashtag_list:
        # we don`t need to check if the tweet already exists, because
        # it has a MTM relationship with tweet
        h = Hashtag.objects.create(name=hashtag)
        h.tweet.add(tweet)
        h.save()


class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ['user', 'text', 'created_at']

    # overwrite the create method, to find the hashtags inside the tweet and create them
    def create(self, validated_data):
        tweet_obj = Tweet.objects.create(**validated_data)
        tweet_obj.save()
        text = validated_data['text']
        process_hashtags(text=text, tweet=tweet_obj)
        return tweet_obj


class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = ['user', 'text', 'created_at', 'reply_to_tweet']


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ['user', 'text', 'created_at', 'quote_to_tweet']
