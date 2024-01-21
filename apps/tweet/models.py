from django.db import models
from django.conf import settings


# TODO create two more classes for tweets that users hav like and do i need a many to many for tweets and tweets
class Tweet(models.Model):
    class TweetType(models.TextChoices):
        TWEET = "tweet", "Tweet"
        REPLY = "reply", "reply"
        RETWEET = "retweet", "retweet"
        QUOTE = "quote", "quote"

    # TODO user, content and created_at are index related fields
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="tweets",
        on_delete=models.CASCADE,
        verbose_name="user",
    )
    text = models.TextField(max_length=350, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # set a parent for tweets
    parent_tweet = models.ForeignKey(
        "Tweet",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="children",
    )

    # a tweet, reply, retweet and quote are the same thing
    type = models.CharField(
        max_length=8, choices=TweetType.choices, default=TweetType.TWEET.value
    )

    # TODO read about annotation and aggregation and function models

    class Meta:
        # check this
        indexes = [models.Index(fields=["user", "created_at"])]

        verbose_name = "tweet"
        verbose_name_plural = "tweets"

    def __str__(self):
        return '"{}" by {} at {}'.format(self.text, self.user, self.created_at)
