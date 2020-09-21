from django.db import models

# Create your models here.


def upload_location(instance, filename):
	return "%s/%s" %(instance.id, filename)


class Post(models.Model):
	title = models.CharField(max_length=100)
	image = models.ImageField(upload_to=upload_location,
			null=True, 
			blank=True, 
			width_field="width_field", 
			height_field="height_field")
	height_field = models.IntegerField(default=0)
	width_field = models.IntegerField(default=0)
	content = models.TextField()
	is_active = models.BooleanField(default=True)
	updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
	created_at = models.DateTimeField(auto_now=False, auto_now_add=True)

	def __str__(self):
		return self.title

