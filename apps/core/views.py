# # django imports
# # python imports
# import re
#
# # outside libs
# import arrow
# from django.contrib.auth import login, authenticate
# from django.shortcuts import get_object_or_404
# from django.shortcuts import render, redirect
# from django.views.decorators.http import require_http_methods
# from django.views.generic.detail import DetailView
#
# # project imports
# from .forms import SignUpForm, CreateTweetForm
# from .models import User, Tweet, Hashtag, Like, Retweet, Relationship
#
#
# '''all these handle query functions should probably be inside a class'''
#
# # define what a single tweet is and looks like
# def handle_single_tweet(item, request_user):
#     to_arrow = arrow.get(item.created_at)
#
#     if Like.objects.filter(user=request_user, tweet=item).exists():
#         like_check = True
#     else:
#         like_check = False
#
#     dic = {
#         'id': item.id,
#         'username': item.user.username,
#         'created_at': to_arrow.humanize(),
#         'text': item.text,
#         'likecount': item.likes_of_tweet.all().count(),
#         'retweetcount': item.retweets.all().count(),
#         'like_check': like_check,
#     }
#
#     if Relationship.objects.filter(from_user=request_user, to_user=item.user).exists():
#         status = Relationship.objects.get(from_user=request_user, to_user=item.user).status
#         if status == 1:
#             dic['status'] = 'following'
#
#     return dic
#
#
# # TODO if i want to do specific code for retweets quotes and likes
# #  i should keep this otherwise these two functions below can be merged into one
# def handle_query_tweets_replies(items, request_user):
#     ls = []
#
#     for t in items:
#
#         dic = {}
#         dic.update(handle_single_tweet(t, request_user=request_user))
#
#         # TODO this could also go through the single tweet handler
#         #  but twitter actually shows tweets like this
#         if t.is_reply == True:
#             dic['reply'] = {
#                 'reply_id': t.reply_to_tweet.id,
#                 'username': t.reply_to_tweet.user,
#                 'text': t.reply_to_tweet.text,
#                 'created_at': t.reply_to_tweet.created_at,
#             }
#         if t.is_quote == True:
#             dic['quote'] = {
#                 'quote_id': t.quote_to_tweet.id,
#                 'username': t.quote_to_tweet.user,
#                 'text': t.quote_to_tweet.text,
#                 'created_at': t.quote_to_tweet.created_at,
#             }
#         ls.append(dic)
#
#     return ls
#
#
# def handle_query_retweets(items, request_user):
#     ls = []
#
#     for t in items:
#         dic = {
#             'retweet_by': t.user,
#         }
#         dic.update(handle_single_tweet(t.tweet, request_user=request_user))
#         ls.append(dic)
#
#     return ls
#
#
# def handle_query_likes(items, request_user):
#     ls = []
#
#     for t in items:
#         dic = {
#             'liked_by': t.user,
#         }
#         dic.update(handle_single_tweet(t.tweet, request_user=request_user))
#         ls.append(dic)
#
#     return ls
#
#
# def handle_query(q, request_user):
#     ls = []
#
#     # send different sections to their own handler function
#     if q['tweets']: ls += handle_query_tweets_replies(q['tweets'], request_user=request_user)
#     if q['retweets']: ls += handle_query_retweets(q['retweets'], request_user=request_user)
#     if q['likes']: ls += handle_query_likes(q['likes'], request_user=request_user)
#
#     return ls
#
#
# def get_the_shit(self):
#     following_qs = self.get_following()
#     data = {}
#
#     for flwr in following_qs:
#         data['tweets'] = [i for i in Tweet.objects.filter(user=flwr)]
#         data['likes'] = [i for i in Like.objects.filter(user=flwr) if i.tweet.user != self]
#         data['retweets'] = [i for i in Retweet.objects.filter(user=flwr)]
#
#     return data
#
#
# def home(request):
#     if request.user.get_the_shit():
#         context = {'object_list': handle_query(request.user.get_the_shit(), request_user=request.user)}
#         return render(request, 'home.html', context)
#     else:
#         return render(request, 'home.html')
#
#
# def entry(request):
#     if request.user.is_authenticated:
#         return redirect('home')
#     else:
#         return redirect('login')
#
#
# def process_hashtags(text, tweet):
#     regex = "#(\w+)"
#     hashtag_list = re.findall(regex, text)
#     for hashtag in hashtag_list:
#         h = Hashtag.objects.create(name=hashtag)
#         h.tweet.add(tweet)
#         h.save()

from rest_framework.response import Response
from rest_framework.decorators import api_view
@api_view()
def entry(request):
    return Response('ok')
