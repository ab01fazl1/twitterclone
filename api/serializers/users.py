from rest_framework import serializers
from apps.user.models import User, Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "name", "date_joined"]


class ProfileSerializer(serializers.ModelSerializer):

    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()
    user = UserSerializer

    class Meta:
        model = Profile
        fields = [
            "user",
            "description",
            "birthday",
            "follower_count",
            "following_count",
        ]

    def get_follower_count(self):
        pass

    def get_following_count(self):
        pass
