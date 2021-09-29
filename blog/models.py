from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
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
