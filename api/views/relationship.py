from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from apps.following.models import Relationship
from api.serializers.relationship import RelationshipSerializer


class RelationshipViews(CreateAPIView, DestroyAPIView):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer


# TODO change this view
class UserRelationshipViews(ListAPIView):
    serializer_class = RelationshipSerializer

    def get_queryset(self):
        return Relationship.objects.filter(from_user=self.kwargs["users_pk"])
