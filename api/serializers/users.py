from rest_framework import serializers
from apps.user.models import User, Profile
from apps.following.services import get_follower_count, get_following_count
from apps.following.models import Relationship


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username", "name", "date_joined"]


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = [
            "description",
            "birthday",
        ]


class GetUserSerializer(serializers.ModelSerializer):

    Profile = ProfileSerializer

    follower_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "date_joined",
            "email",
            "profile",
            "follower_count",
            "following_count",
        ]

    def get_follower_count(self, user_obj: User):
        return Relationship.objects.filter(from_user=user_obj).count()

    def get_following_count(self, user_obj: User):
        return Relationship.objects.filter(to_user=user_obj).count()
