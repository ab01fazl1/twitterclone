from django.db import models


# from tweet.models import Tweet


class Hashtag(models.Model):
    name = models.CharField(max_length=100)
    tweet = models.ManyToManyField("tweet.Tweet", related_name="tweets")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "hashtag"
        verbose_name_plural = "hashtags"
