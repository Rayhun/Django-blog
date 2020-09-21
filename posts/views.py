from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404 , redirect
from django.urls import reverse
from django.core.paginator import Paginator

# from myapp.models import Contact

# Create your views here.
from .forms import PostForm #  Dont Undestent form.py
from .models import Post
 
def post_home(request):
	instence = Post.objects.all()
	instence = Paginator(instence, 4) # Show 25 contacts per page.
	
	page_number = request.GET.get('page')
	instence = instence.get_page(page_number)
	contex = {
		'object_list': instence
	}
	return render(request, 'base.html', contex)
    
def post_create(request):
	form = PostForm(request.POST or None, request.FILES or None)
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
	instence = get_object_or_404(Post,pk=pk)
	context = {
		"name": instence.title,
		"instence":instence,
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
		form = PostForm(request.POST or None , request.FILES or None, instance = instence )
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, "Update Success")
		else:
			messages.error(request, "Update Not Success")
		context = {
			"object":instence,
			"form":form,
		}
		return redirect('post_detail', pk=pk)

def post_delete(request,pk):
	quryis = get_object_or_404(Post,pk=pk)
	quryis.delete()
	messages.success(request, "Delete Success")
	return redirect ('post_home')