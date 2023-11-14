from django.urls import path, include
from views import TweetView, ReplyView, QuoteView, tweet_like_list_view, tweet_retweet_list_view, tweet_quote_list_view

url_patterns = [
    # endpoints that go to the tweetview
    path('<str:username>/tweet/<int:pk>/', TweetView.as_view(), name='tweet_detail_view'),
    path('create_tweet/', TweetView.as_view(), name='create_tweet'),
    path('delete_tweet/<int:pk>/', TweetView.as_view(), name='delete_tweet'),

    # reply endpoints
    path('create_reply/<int:tweet_pk>/', ReplyView.as_view(), name='create_reply'),
    path('reply/<int:pk>/', ReplyView.as_view(), 'reply_detail_view'),
    path('delete_reply/<int:pk>/', ReplyView.as_view(), 'delete_reply'),

    # quote endpoints
    path('create_quote/<int:pk>/', QuoteView.as_view(), name='create_quote'),
    path('delete_quote/<int:pk>/', QuoteView.as_view(), name='delete_quote'),
    path('quote/<int:pk>/', QuoteView.as_view(), name='quote_view'),

    # endpoints to call queries for a specific tweet
    path('<str:username>/tweet/<int:tweet_pk>/likes_list/', tweet_like_list_view, name='tweet_like_list'),
    path('<str:username>/tweet/<int:tweet_pk>/retweets_list/', tweet_retweet_list_view, name='tweet_retweet_list'),
    path('<str:username>/tweet/<int:tweet_pk>/quotes_list/', tweet_quote_list_view, name='tweet_quote_list'),
]