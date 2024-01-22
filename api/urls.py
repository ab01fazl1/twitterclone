from django.urls import path, include
from rest_framework_nested import routers

# url patterns that I want
# /login/
# /user/tweets/
# tweet/pk/likes

from .views.tweets import (
    CreateTweetView,
    CreateReplyView,
    CreateRetweetView,
    CreateQuoteView,
    GetTweetView,
)
from .views.users import (
    CreateUserView,
    GetUserView,
    ResetPasswordView,
    UpdateProfileView,
    UpdateUserView,
)
from .views.like import LikeView
from .views.hashtag import HashtagListView
from .views.relationship import FollowView, UnfollowView, BlockView

"""

url patterns explanation:

1. for urls i prefer to write my own urls with my own path names
this is because i feel like the urls will be more human readable and easier to understand
and i didnt use drf routers because im not using viewsets in my views

"""

tweet_patterns = [
    path("create_tweet/", CreateTweetView.as_view()),
    path("create_reply/", CreateReplyView.create),
    # path("create_retweet/", CreateRetweetView.create),
    path("create_quote/", CreateQuoteView.create),
    path("tweet/<int:pk>/", GetTweetView.as_view(), name="tweet_view"),
]

user_patterns = [
    path("create_user/", CreateUserView.as_view(), name="create-user"),
    path("user/<int:pk>/", GetUserView.as_view(), name="user-view"),
    # path("update_profile/", UpdateProfileView.as_view(), name="update-profile"),
    # path("update_user/", UpdateUserView.as_view(), name="update-user"),
    # path("reset_password/", ResetPasswordView.as_view(), name="reset-password"),
]

like_patterns = [
    path("like/", LikeView.as_view(), name="like"),
]

hashtag_patterns = [
    path("hashtag/<int:pk>/", HashtagListView.as_view(), name="hashtag"),
]

relationship_patterns = [
    # path('follow/', FollowView.as_view(), name='Follow'),
    # path('unfollow/', UnfollowView.as_view(), name='Unfollow'),
    # path('block/', BlockView.as_view(), name='Block'),
]

urlpatterns = (
    [
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]
    + tweet_patterns
    + user_patterns
    + hashtag_patterns
    + relationship_patterns
    + like_patterns
)
