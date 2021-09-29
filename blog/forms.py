from django.db import models
from django import forms
from .models import ReplayBlogComment, BlogComment


class CommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'mobile', 'website', 'image', 'message']


class ReplayCommentForm(forms.ModelForm):
    class Meta:
        model = ReplayBlogComment
        fields = ['name', 'email', 'mobile', 'website', 'image', 'message']
