from api.serializers.hashtag import HashtagSerializer
from rest_framework.generics import CreateAPIView, DestroyAPIView
from apps.hashtag.models import Hashtag


class HashtagViewSet(CreateAPIView, DestroyAPIView):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
