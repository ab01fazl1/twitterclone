from django.db import models

def create_tweet(self,text):
    return Tweet.objects.create(user=self,text=text)

def delete_tweet(self,tweet_obj):
    id = tweet_obj.id
    Tweet.objects.filter(
        user=self,
        id=id
    ).delete()
    return

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

def create_reply(request, tweet_pk):
    tweet_obj = get_object_or_404(Tweet, id=tweet_pk)
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data.get('text')
            user = request.user
            tweet = Tweet.objects.create(user=user, text=text, is_reply=True, reply_to_tweet=tweet_obj)
            tweet.save()
            process_hashtags(text, tweet)

            return redirect('home')  # TODO maybe send to a page that says tweet created or go to home
        else:
            return 'form is not valid'  # TODO go back to the create tweet page and display an error

    else:
        form = CreateTweetForm()

    return render(request, 'create_reply.html', {'form': form, 'tweet_obj': tweet_obj})


def quote(request, tweet_pk):
    tweet_obj = get_object_or_404(Tweet, id=tweet_pk)
    if request.method == 'POST':
        form = CreateTweetForm(request.POST)
        if form.is_valid():

            text = form.cleaned_data.get('text')
            user = request.user
            tweet = Tweet.objects.create(user=user, text=text, is_quote=True, reply_to_quote=tweet_obj)
            tweet.save()
            process_hashtags(text, tweet)

            return redirect('home')
        else:
            return 'form is not valid'

    else:
        form = CreateTweetForm()

    return render(request, 'create_quote.html', {'form': form, 'tweet_obj': tweet_obj})


def retweet(request, tweet_pk):
    t = get_object_or_404(Tweet, id=tweet_pk)

    if Retweet.objects.filter(user=request.user, tweet=t).exists():
        Retweet.objects.filter(user=request.user, tweet=t).delete()
    else:
        Retweet.objects.create(user=request.user, tweet=t)

    return redirect('/')
