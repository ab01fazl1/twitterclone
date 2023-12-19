from django.urls import path, include
from .views import entry
from rest_framework_nested import routers

# views imports
from user.views import UserViewSet
from tweet.views import TweetUserViewSet, TweetView
from like.views import LikeViewSet
from Hashtag.views import HashtagViewSet
from following.views import RelationshipViews, UserRelationshipViews

# users and users_tweets routes
router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename="users")
users_router = routers.NestedDefaultRouter(router, 'users', lookup='users')
users_router.register(r'tweets', TweetUserViewSet, basename='tweets')

# tweets and tweets_likes router
router.register(r'tweet', TweetView, basename='tweet')
like_router = routers.NestedDefaultRouter(router, 'tweet', lookup='tweet')
like_router.register(r'likes', LikeViewSet, basename='like')

# hashtags routes
router.register(r'hashtags', HashtagViewSet, basename='hashtags')

# relationship router for follow, unfollow, block and listings of the relationships
# TODO: find out if there is a better name for this route
router.register(r'action', RelationshipViews, basename='action')

# this is for the user/following, user/follower routes
users_router.register(r'list', UserRelationshipViews, basename='list')


urlpatterns = [
    # routers
    path('', include(router.urls)),
    path('', include(users_router.urls)),
    path('', include(like_router.urls)),

    # core
    path('', entry, name='entry'),
]
