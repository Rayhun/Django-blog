from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404 , redirect

# Create your views here.
from .forms import PostForm
from .models import Post
 
def post_home(request):
	queryset = Post.objects.all()
	context = {
		"object_list":queryset,
		"page_title": "Home Page"
	}
	return render(request,"base.html", context)


def post_create(request):
	form = PostForm(request.POST or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		messages.success(request, "Success Created")
		return redirect ('post_home')
	else:
		messages.error(request, "Not Success Created")
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
	return render(request,"single.html", context)


def post_list(request):
	context = {
		"name": "List"
	}
	return render(request,"base.html", context)


def post_update(request,pk):
	if request.method == 'GET':
		instence = get_object_or_404(Post,pk=pk)
		form = PostForm(instance = instence )
		context = {
			"object":instence,
			"form":form,
		}
		return render(request,"post-update.html", context)
	else:	
		instence = get_object_or_404(Post,pk=pk)
		form = PostForm(request.POST or None, instance = instence )
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Update Success")
			# return redirect ('post_home')
		else:
			messages.error(request, "Update Not Success")
		context = {
			"object":instence,
			"form":form,
		}
		return render(request,"post-update.html", context)

def post_delete(request,pk):
	quryis = get_object_or_404(Post,pk=pk)
	quryis.delete()
	messages.success(request, "Delete Success")
	return redirect ('post_home')
	# context = {
	# 	"name": "Delete"
	# }