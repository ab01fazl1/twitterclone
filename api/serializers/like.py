from rest_framework import serializers
from apps.like.models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ["tweet", "user", "created_at"]
