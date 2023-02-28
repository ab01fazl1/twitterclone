from django.contrib.auth.forms import UserCreationForm
from .models import User,Tweet
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)


class CreateTweetForm(forms.Form):
    # class Meta:
    #     model = Tweet
    #     fields = ('text',)
    text = forms.CharField(label='text',max_length=350)
    # reply = forms.HiddenInput()