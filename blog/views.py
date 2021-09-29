from django.db import models
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from .models import BlogPost


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
        self.object.total_view += 1
        self.object.save()
        return super().get_context_data(*args, **kwargs)
