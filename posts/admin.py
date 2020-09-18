from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
	list_display = ['id', "title","content", "is_active"]
	list_display_links = ('id',)
	list_filter = ['created_at']
	list_editable = ('title',)
	readonly_fields = ('created_at', 'updated_at')

admin.site.register(Post,PostAdmin)