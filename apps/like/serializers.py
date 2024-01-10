from rest_framework import serializers
from .models import Like


# from tweet.serializers import TweetSerializer
# from user.serializers import UserSerialzer

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['tweet', 'user', 'created_at']
    #
    # tweet = TweetSerializer()
    # user = UserSerializer()
