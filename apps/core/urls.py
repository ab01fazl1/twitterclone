from django.urls import path, include
from .views import entry
from rest_framework_nested import routers
from user.views import UserViewSet
from tweet.views import TweetUserViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
users_router = routers.NestedDefaultRouter(router, 'users', lookup='users')
users_router.register(r'tweets', TweetUserViewSet, basename='tweets')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(users_router.urls)),
    # core
    path('', entry, name='entry'),

    # users
    # path('', include('user.urls')),

    # tweet
    # path('', include('tweet.urls')),
]
