from django.db import models
from django.conf import settings

# Create your models here.
class Tweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='tweets', on_delete=models.CASCADE)
    text = models.TextField(max_length=350)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '"{}" by {} at {}'.format(self.text, self.user, self.created_at)

class Reply(Tweet):
    reply_to_tweet = models.ForeignKey(Tweet, related_name='replies', on_delete=models.CASCADE)

class Quote(Tweet):
    quote_to_tweet = models.ForeignKey(Tweet, related_name='quotes', on_delete=models.CASCADE)

class Retweet(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='retweets_by_user',on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='retweets',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

