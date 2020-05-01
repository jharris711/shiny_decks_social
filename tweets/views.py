from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
# Create your views here.

from .models import Tweet


def home_view(request, *args, **kwargs):
    return HttpResponse("<h1>Hello World!</h1>")


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    #REST API VIEW
    data = {
        "id": tweet_id,
    }
    status = 200
    try:
        tweet = Tweet.objects.get(id=tweet_id)
        data['content'] = tweet.content
    except:
        data['message'] = "Not Found"
        status = 404

    return JsonResponse(data, status=status)
