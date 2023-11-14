from django.urls import path, include
from user import urls
from tweet import urls

# from django.contrib.auth import views as auth_views
# from django.contrib.auth.decorators import login_required
#
# from .views import signup,create_tweet,create_reply,\
#     profile_view,profile_view_with_replies,home,entry,tweet_detail_view,\
#     like,quote,tweet_like_list,tweet_quote_list,tweet_retweet_list,follow,unfollow
#
#
# # from .views import testhome
#
urlpatterns = [
#     # core
#     path('', entry, name='entry'),
#     path('home/',login_required(home),name='home'),
#
    # users
    path('', include('user.urls')),

    # tweet
    path('', include('tweet.urls')),
#
#     # relationship
#     path('<str:username>/follow/', follow, name='follow'),
#     path('<str:username>/unfollow/', unfollow, name='unfollow'),
#
#     # like
#     path('like/<int:tweet_pk>/', login_required(like), name='like'),
]
#
# # path('api-auth/', include('rest_framework.urls'))