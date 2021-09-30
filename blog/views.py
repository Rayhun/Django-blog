from django.db import models
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import BlogPost, BlogComment
from .forms import ReplayCommentForm, CommentForm


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
        context['comment'] = BlogComment.objects.filter(
            post=self.object, parent__isnull=True
        )
        context['comment_count'] = BlogComment.objects.filter(
            post=self.object
        ).count()
        context['form'] = CommentForm()
        context['replay_blog'] = BlogComment.objects.filter(parent=20)
        self.object.total_view += 1
        self.object.save()
        return context

    def post(self, request, pk):
        object = self.model.objects.get(pk=pk)
        try:
            replay_comment = int(request.POST.get('replay_comment'))
            replay = BlogComment.objects.get(pk=replay_comment)
        except Exception as e:
            print(e)
            replay_comment = None
            replay = None
        # comment = BlogComment.objects.get(pk=20)
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.post = object
            user.parent = replay
            user.save()
            return redirect('blog_details', pk=pk)
        return render(request, self.template_name)
