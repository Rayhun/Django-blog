from django.db import models

# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	is_active = models.BooleanField(default=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title
