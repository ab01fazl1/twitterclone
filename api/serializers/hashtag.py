from rest_framework import serializers
from apps.hashtag.models import Hashtag


class HashtagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hashtag
        fields = ["name", "tweet", "created_at"]
