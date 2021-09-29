from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField


class Category(models.Model):
    name = CharField(max_length=250, unique=True)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    ''' Create Post Models '''
    author = models.ForeignKey(
        User, on_delete=SET_NULL, null=True, related_name='author'
    )
    title = models.CharField(max_length=500)
    category = models.ForeignKey(
        Category, on_delete=SET_NULL, null=True, related_name='category'
    )
    image = models.ImageField(upload_to='media')
    description = models.TextField()
    total_view = models.PositiveBigIntegerField(default=0)
    create_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)
    is_hot = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=SET_NULL, related_name='blog', null=True
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=25, blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to="comment_image", null=True)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now=True, null=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class ReplayBlogComment(models.Model):
    comment = models.ForeignKey(
        BlogComment, on_delete=SET_NULL, related_name='replay_blog', null=True
    )
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    mobile = models.CharField(max_length=25, blank=True)
    website = models.URLField(blank=True)
    image = models.ImageField(upload_to="comment_image", null=True)
    message = models.TextField()
    create_at = models.DateTimeField(auto_now=True, null=True)
    update_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name
