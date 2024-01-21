from .models import Tweet
from apps.hashtag.models import Hashtag
import re


def process_hashtags(text, tweet_obj):
    regex = "#(\w+)"
    hashtag_list = re.findall(regex, text)
    for hashtag in hashtag_list:
        h = Hashtag.objects.get_or_create(name=hashtag)
        h.tweet.add(tweet_obj)
        h.save()


def create_tweet(user, text):
    tweet = Tweet.objects.create(user=user, text=text)
    process_hashtags(text, tweet)


def create_quote(user, text, tweet_pk):
    tweet_obj = Tweet.objects.filter(pk=tweet_pk)
    quote = Tweet.objects.create(
        user=user, text=text, parent_tweet=tweet_obj, type=Tweet.TweetType.QUOTE.value
    )
    process_hashtags(text, quote)


def create_reply(user, text, tweet_pk):
    tweet_obj = Tweet.objects.filter(pk=tweet_pk)
    reply = Tweet.objects.create(
        user=user, text=text, parent_tweet=tweet_obj, type=Tweet.TweetType.REPLY.value
    )
    process_hashtags(text, reply)


def create_retweet(user, tweet_obj):
    retweet = Tweet.objects.create(
        user, parent_tweet=tweet_obj, type=Tweet.TweetType.RETWEET.value
    )
