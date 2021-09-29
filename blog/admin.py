from django.contrib import admin
from .models import Category, BlogPost, BlogComment, ReplayBlogComment


class AdminCategory(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, AdminCategory)


class AdminBlogPost(admin.ModelAdmin):
    list_display = ['author', 'title', 'category', 'total_view']
admin.site.register(BlogPost, AdminBlogPost)


class AdminBlogComment(admin.ModelAdmin):
    list_display = ['post', 'name', 'email', 'mobile']
admin.site.register(BlogComment, AdminBlogComment)

class AdminReplayBlogComment(admin.ModelAdmin):
    list_display = ['comment', 'name', 'email', 'mobile']
admin.site.register(ReplayBlogComment, AdminReplayBlogComment)
