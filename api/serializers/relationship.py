from apps.following.models import Relationship
from rest_framework import serializers


class RelationshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relationship
        fields = ["from_user", "to_user", "status", "created_at"]
