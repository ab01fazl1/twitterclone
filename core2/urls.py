from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from .views import signup,create_tweet,create_reply,\
    profile_view,profile_view_with_replies,home,entry,tweet_detail_view,\
    like,quote,tweet_like_list,tweet_quote_list,tweet_retweet_list,follow,unfollow


# from .views import testhome

urlpatterns = [
    path('', entry, name='entry'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'),
    path('home/',login_required(home),name='home'),


    path('create_tweet/', login_required(create_tweet), name='create_tweet'),
    path('create_reply/<int:tweet_pk>/', login_required(create_reply), name='create_reply'),
    path('create_quote/<int:tweet_pk>/', login_required(quote), name='create_quote'),

    path('<str:username>/', profile_view.as_view(),name='profile_view'),

    path('<str:username>/follow/', follow, name='follow'),
    path('<str:username>/unfollow/', unfollow, name='unfollow'),
    path('<str:username>/tweet/<int:tweet_pk>/', tweet_detail_view,name='tweet_detail_view'),
    path('<str:username>/tweet/<int:tweet_pk>/likes_list/', tweet_like_list,name='tweet_like_list'),
    path('<str:username>/tweet/<int:tweet_pk>/retweets_list/', tweet_retweet_list,name='tweet_retweet_list'),
    path('<str:username>/tweet/<int:tweet_pk>/quotes_list/', tweet_quote_list,name='tweet_quote_list'),

    path('<str:username>/with_replies/', profile_view_with_replies.as_view(),name='profile_view_with_replies'),

    path('like/<int:tweet_pk>/', login_required(like), name='like'),
]