from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_NULL
from django.db.models.fields import CharField


class IpStore(models.Model):
    ip_name = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    ip_type = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.CharField(max_length=100, null=True, blank=True)
    timezone = models.CharField(max_length=100, null=True, blank=True)
    isp = models.CharField(max_length=100, null=True, blank=True)
    org = models.CharField(max_length=100, null=True, blank=True)
    ass = models.CharField(max_length=100, null=True, blank=True)
    lat = models.CharField(max_length=100, null=True, blank=True)
    lon = models.CharField(max_length=100, null=True, blank=True)
    query = models.CharField(max_length=100, null=True, blank=True)
    status = models.CharField(max_length=100, null=True, blank=True)
    countryCode = models.CharField(max_length=100, null=True, blank=True)
    create_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.ip_name


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
    like = models.ManyToManyField(IpStore, related_name='like')

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    post = models.ForeignKey(
        BlogPost, on_delete=SET_NULL, related_name='blog', null=True
    )
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=SET_NULL)
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
    
    def children(self):
        return BlogComment.objects.filter(parent=self)
    
    @classmethod
    def is_parent(self):
        if self.parent.field.name is not None:
            return False
        return True


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
