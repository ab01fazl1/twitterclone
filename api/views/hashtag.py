from api.serializers.hashtag import HashtagSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView, ListAPIView
from apps.hashtag.models import Hashtag


# TODO check if i need this
# do we even delete hashtags?
# class HashtagViewSet(CreateAPIView, DestroyAPIView):


class HashtagListView(ListAPIView):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
