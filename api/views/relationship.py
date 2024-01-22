from rest_framework.generics import CreateAPIView, DestroyAPIView
from apps.following.models import Relationship
from api.serializers.relationship import RelationshipSerializer


# class RelationshipViews(CreateAPIView, DestroyAPIView):
# queryset = Relationship.objects.all()
# serializer_class = RelationshipSerializer


class FollowView(CreateAPIView):
    serializer_class = RelationshipSerializer


class UnfollowView(DestroyAPIView):
    serializer_class = RelationshipSerializer


class BlockView(CreateAPIView):
    serializer_class = RelationshipSerializer
