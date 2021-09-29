from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import BlogPost, BlogComment


class BlogHomePageView(TemplateView):
    template_name = 'home.html'
    model = BlogPost

    def get_context_data(self, **kwargs):
        context = super(BlogHomePageView, self).get_context_data(**kwargs)
        context['last_post'] = self.model.objects.first()
        context['first_four'] = self.model.objects.all()[1:6]
        context['top_popular_post'] = self.model.objects.all().order_by(
            '-total_view'
        )[:1]
        context['popular_post'] = self.model.objects.all().order_by(
            '-total_view'
        )
        return context


class BlogDetails(DetailView):
    template_name = 'details.html'
    model = BlogPost

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['comment'] = BlogComment.objects.filter(post=self.object)
        self.object.total_view += 1
        self.object.save()
        return context

    def post(self, request, pk):
        object = self.model.objects.get(pk=pk)
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        website = request.POST.get('website')
        image = request.FILES.get('image')
        message = request.POST.get('message')
        comment = BlogComment.objects.filter(post__pk=pk)
        if name and email and message:
            BlogComment.objects.create(
                name=name, email=email, mobile=mobile, website=website,
                message=message, post=object, image=image
            )
            context = {
                'object': object,
                'comment': comment
            }
            return render(request, self.template_name, context)
        return render(request, self.template_name)
