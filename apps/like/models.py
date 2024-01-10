from django.db import models
from twitter.apps.tweet.models import Tweet
from django.conf import settings


# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes_of_user', on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet, related_name='likes_of_tweet', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} liked tweet id:{} by {}'.format(self.user, self.tweet.id, self.tweet.user)

    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'
