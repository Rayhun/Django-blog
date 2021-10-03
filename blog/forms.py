from django.db import models
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ReplayBlogComment, BlogComment


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    image = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'email', 'image',
            'password1', 'password2',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'mobile', 'website', 'image', 'message']


class ReplayCommentForm(forms.ModelForm):
    class Meta:
        model = ReplayBlogComment
        fields = ['name', 'email', 'mobile', 'website', 'image', 'message']
