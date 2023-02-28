# django imports
from django.shortcuts import render, redirect,HttpResponse
from django.contrib.auth import login, authenticate
# from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.utils import timezone

# python imports
from datetime import datetime,timedelta
import re

# outside libs
import arrow

# project imports
from .forms import SignUpForm,CreateTweetForm
from .models import User,Tweet,Hashtag,Like,Retweet,Relationship


'''all these handle query functions should probably be inside a class'''
#define what a single tweet is and looks like
def handle_single_tweet(item,request_user):

    to_arrow = arrow.get(item.created_at)

    if Like.objects.filter(user=request_user,tweet=item).exists():
        like_check = True
    else:
        like_check = False


    dic = {
        'id': item.id,
        'username': item.user.username,
        'created_at': to_arrow.humanize(),
        'text': item.text,
        # commentcount:'',
        'likecount': item.likes_of_tweet.all().count(),
        'retweetcount': item.retweets.all().count(),
        'like_check':like_check,
    }

    if Relationship.objects.filter(from_user=request_user,to_user=item.user).exists():
        status = Relationship.objects.get(from_user=request_user,to_user=item.user).status
        if status == 1:
            dic['status'] = 'following'

    return dic

# TODO if i want to do specific code for retweets quotes and likes
#  i should keep this otherwise these two functions below can be merged into one
def handle_query_tweets_replies(items,request_user):

    ls = []

    for t in items:

        dic = {}
        dic.update(handle_single_tweet(t,request_user=request_user))

        # TODO this could also go through the single tweet handler
        #  but twitter actually shows tweets like this
        if t.is_reply == True:
            dic['reply'] = {
                'reply_id':t.reply_to_tweet.id,
                'username': t.reply_to_tweet.user,
                'text': t.reply_to_tweet.text,
                'created_at': t.reply_to_tweet.created_at,
            }
        if t.is_quote == True:
            dic['quote'] = {
                'quote_id': t.quote_to_tweet.id,
                'username': t.quote_to_tweet.user,
                'text': t.quote_to_tweet.text,
                'created_at': t.quote_to_tweet.created_at,
            }
        ls.append(dic)

    return ls


def handle_query_retweets(items,request_user):

    ls = []

    for t in items:
        dic = {
            'retweet_by': t.user,
        }
        dic.update(handle_single_tweet(t.tweet,request_user=request_user))
        ls.append(dic)

    return ls


def handle_query_likes(items,request_user):

    ls = []

    for t in items:
        dic = {
            'liked_by': t.user,
        }
        dic.update(handle_single_tweet(t.tweet,request_user=request_user))
        ls.append(dic)

    return ls

def handle_query(q,request_user):

    ls = []

    #send different sections to their own handler function
    if q['tweets']: ls += handle_query_tweets_replies(q['tweets'],request_user=request_user)
    if q['retweets']: ls += handle_query_retweets(q['retweets'],request_user=request_user)
    if q['likes']: ls += handle_query_likes(q['likes'],request_user=request_user)

    #sort --> the problem is that i am humanizing it in the /
    #tweet handler function and now i cant sort based  on that
    # def get_date(d):
    #     return d['created_at']
    # ls.sort(key=get_date)

    return ls


class profile_view(DetailView):
    model = User
    template_name = 'profile.html'

    def get_object(self):
        UserName = self.kwargs.get('username')
        return get_object_or_404(User,username__iexact=UserName)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tweets_list = self.object.tweets.filter(is_reply=False)
        context['tweets'] = handle_query_tweets_replies(tweets_list,request_user=self.request.user)
        return context

class profile_view_with_replies(profile_view):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        tweets_list = self.object.tweets.filter(is_reply=True)
        context['tweets'] = handle_query_tweets_replies(tweets_list,request_user=self.request.user)
        return context

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(request, username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
            else:
                print("user is not authenticated")

            return redirect('/') # TODO this should be changed
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def home(request):
    if request.user.get_the_shit():
        context = {'object_list':handle_query(request.user.get_the_shit(),request_user=request.user)}
        return render(request,'home.html',context)
    else:
        return render(request,'home.html')

def entry(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return redirect('login')



def tweet_detail_view(request,username,tweet_pk):
    t = get_object_or_404(Tweet,user__iexact=username,id=tweet_pk)


def like(request,tweet_pk):

    t = get_object_or_404(Tweet,id=tweet_pk)

    if Like.objects.filter(user=request.user,tweet=t).exists():
        Like.objects.filter(user=request.user,tweet=t).delete()
    else:
        Like.objects.create(user=request.user,tweet=t)

    return redirect('/')


def process_hashtags(text, tweet):
    regex = "#(\w+)"
    hashtag_list = re.findall(regex, text)
    for hashtag in hashtag_list:
        h = Hashtag.objects.create(name=hashtag)
        h.tweet.add(tweet)
        h.save()


def create_tweet(request):
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data.get('text')
            user = request.user
            tweet = Tweet.objects.create(user=user, text=text)  # TODO or i can just write user.create_tweet
            tweet.save()
            process_hashtags(text, tweet)

            return redirect('home')  # TODO maybe send to a page that says tweet created or go to home
        else:
            return 'form is not valid'  # TODO go back to the create tweet page and display an error

    else:
        form = CreateTweetForm()

    return render(request, 'create_tweet.html', {'form': form})



def create_reply(request,tweet_pk):
    tweet_obj = get_object_or_404(Tweet,id=tweet_pk)
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data.get('text')
            user = request.user
            tweet = Tweet.objects.create(user=user, text=text, is_reply=True, reply_to_tweet=tweet_obj)
            tweet.save()
            process_hashtags(text, tweet)

            return redirect('home')  # maybe send to a page that says tweet created or go to home
        else:
            return 'form is not valid'  # go back to the create tweet page and display an error

    else:
        form = CreateTweetForm()

    return render(request, 'create_reply.html', {'form': form,'tweet_obj':tweet_obj})

def quote(request,tweet_pk):
    tweet_obj = get_object_or_404(Tweet, id=tweet_pk)
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data.get('text')
            user = request.user
            tweet = Tweet.objects.create(user=user, text=text, is_quote=True, reply_to_quote=tweet_obj)
            tweet.save()
            process_hashtags(text, tweet)

            return redirect('home')  # maybe send to a page that says tweet created or go to home
        else:
            return 'form is not valid'  # go back to the create tweet page and display an error

    else:
        form = CreateTweetForm()

    return render(request, 'create_quote.html', {'form': form, 'tweet_obj': tweet_obj})

def retweet(request,tweet_pk):
    t = get_object_or_404(Tweet, id=tweet_pk)

    if Retweet.objects.filter(user=request.user, tweet=t).exists():
        Retweet.objects.filter(user=request.user, tweet=t).delete()
    else:
        Retweet.objects.create(user=request.user, tweet=t)

    return redirect('/')


def tweet_like_list(request,username,tweet_pk):
    t = Tweet.objects.filter(id=tweet_pk)
    likes = Like.objects.filter(tweet=t)
    return render(request,'tweet_like_list.html',{'likes':likes})

def tweet_quote_list(request,username,tweet_pk):
    t = Tweet.objects.filter(id=tweet_pk)
    quotes = Tweet.objects.filter(quote_to_tweet=t)
    return render(request,'tweet_quote_list.html',{'quotes':quotes})

def tweet_retweet_list(request,username,tweet_pk):
    t = Tweet.objects.filter(id=tweet_pk)
    likes = Retweet.objects.filter(tweet=t)
    return render(request,'tweet_retweet_list.html',{'Retweet':Retweet})







#this could be a function to serve tweet_detail_view
def show_comments(request):
    pass







def follow(request,username):
    u = User.objects.get(username__iexact=username)
    Relationship.objects.create(from_user=request.user,to_user=u,status=1)
    return redirect('/')

def unfollow(request,username):
    u = User.objects.get(username__iexact=username)
    Relationship.objects.get(from_user=request.user,to_user=u,status=1).delete()
    return redirect('/')




