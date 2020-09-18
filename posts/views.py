from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404

# Create your views here.
from .forms import PostForm
from .models import Post
 
def post_home(request):
	queryset = Post.objects.all() #Post Why?
	context = {
		"object_list":queryset,
		"page_title": "Home Page"
	}

	return render(request,"index.html", context)

def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
	context = {
		"form": form,
	}
	return render(request,"post-form.html", context)

def post_detale(request,pk):
	quryis = get_object_or_404(Post,pk=pk)
	context = {
		"name": quryis.title,
		"quryis":quryis,
	}
	return render(request,"post-create.html", context)

def post_list(request):
	context = {
		"name": "List"
	}
	return render(request,"index.html", context)

def post_update(request):
	context = {
		"name": "Update"
	}
	return render(request,"post-update.html", context)

def post_delete(request):
	context = {
		"name": "Delete"
	}
	return render(request,"index.html", context)