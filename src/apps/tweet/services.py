# @require_http_methods(["GET"])
# def tweet_like_list(request, tweet_pk):
#     t = Tweet.objects.filter(id=tweet_pk)
#     likes = Like.objects.filter(tweet=t)
#     return render(request, 'tweet_like_list.html', {'likes': likes})

# TODO replace this with a rest framework view that sends stuff from query.py
# @require_http_methods(["GET"])
# def tweet_quote_list(request, tweet_pk):
#     t = Tweet.objects.filter(id=tweet_pk)
#     quotes = Tweet.objects.filter(quote_to_tweet=t)
#     return render(request, 'tweet_quote_list.html', {'quotes': quotes})


# @require_http_methods(["GET"])
# def tweet_retweet_list(request, tweet_pk):
#     t = Tweet.objects.filter(id=tweet_pk)
#     retweets = Retweet.objects.filter(tweet=t)
#     return render(request, 'tweet_retweet_list.html', {'Retweet': retweets})