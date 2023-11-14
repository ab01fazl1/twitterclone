from .models import Tweet, Quote, Reply, Retweet
from like.models import Like

# the likes of a tweet
def tweet_like_list(user, tweet_pk):
    pass

def tweet_quote_list(user, tweet_pk):
    return Quote.objects.filter(quote_to_tweet__tweet__pk=tweet_pk)

def tweet_retweet_list(user, tweet_pk):
    pass

def tweet_reply_list(user, tweet_pk):
    pass