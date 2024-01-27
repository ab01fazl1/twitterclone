from rest_framework.generics import CreateAPIView, DestroyAPIView
from apps.following.models import Relationship
from api.serializers.relationship import RelationshipSerializer
from rest_framework.response import Response


class FollowView(CreateAPIView):
    serializer_class = RelationshipSerializer


class UnfollowView(DestroyAPIView):
    serializer_class = RelationshipSerializer


class BlockView(CreateAPIView):
    serializer_class = RelationshipSerializer
