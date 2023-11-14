from django.db import models
from tweet.models import Tweet
from user.models import User

# Create your models here.
class Like(models.Model):
    user = models.ForeignKey(User,related_name='likes_of_user',on_delete=models.CASCADE)
    tweet = models.ForeignKey(Tweet,related_name='likes_of_tweet',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{} liked tweet id:{} by {}'.format(self.user,self.tweet.id,self.tweet.user)
