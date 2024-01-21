from django.urls import path, include
from rest_framework.routers import DefaultRouter

# url patterns that I want
# /api
# user related endpoints
# /create_user/
# /login/
# follow/
# unfollow/
# block/
# /user/username/ - this shows profile
# /user/tweets/
# /user/tweet/pk/ tweet_detail
# /user/tweet/pk/likes
# /create_tweet/
# /create_reply/
# /create_quote/
# /retweet/

from .views.tweets import (
    CreateTweetView,
    CreateReplyView,
    CreateRetweetView,
    CreateQuoteView,
    GetTweetView,
)
from .views.users import (
    GetProfileView,
    CreateUserView,
    ResetPasswordView,
    UpdateProfileView,
    UpdateUserView,
)

router = DefaultRouter()

tweet_patterns = [
    path("create_tweet/", CreateTweetView.as_view()),
    path("create_reply/", CreateReplyView.create),
    path("create_retweet/", CreateRetweetView.create),
    path("create_quote/", CreateQuoteView.create),
    path("tweet/<int:pk>/", GetTweetView.as_view(), name="tweet_view"),
]

user_patterns = [
    path("create_user/", CreateUserView.as_view(), name="create-user"),
    path("user/<int:pk>/", GetProfileView.as_view(), name="profile-view"),
    path("update_profile/", UpdateProfileView.as_view(), name="update-profile"),
    path("update_user/", UpdateUserView.as_view(), name="update-user"),
    path("reset_password/", ResetPasswordView.as_view(), name="reset-password"),
]

urlpatterns = (
    [
        path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    ]
    + tweet_patterns
    + user_patterns
    + router.urls
)
