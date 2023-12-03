from rest_framework.viewsets import ModelViewSet
from .serializers import HashtagSerializer
from .models import Hashtag


class HashtagViewSet(ModelViewSet):
    serializer_class = HashtagSerializer
    queryset = Hashtag.objects.all()
