from django import forms
from .models import Tweet
from django.conf import settings


MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH

MAX_TWEET_LENGTH = 240

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']

    def clean_content(self):
        content = self.cleaned_data.get('content')
        if len(content) > MAX_TWEET_LENGTH:
            raise forms.ValidationError("This post is too long!")
        return content