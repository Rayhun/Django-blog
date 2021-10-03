from ipware import get_client_ip
import json, urllib
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, DetailView
from .models import BlogPost, BlogComment, IpStore
from .forms import CommentForm, SignUpForm
from django.contrib.auth import login, logout


class UserCreateView(TemplateView):
    template_name = 'signup.html'

    def get(self, request):
        form = SignUpForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, form.instance)
            return redirect('/')
        return render(request, self.template_name, {'form': form})

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
        clint_ip, is_routable = get_client_ip(self.request)
        if clint_ip is None:
            clint_ip = "0.0.0.0"
        else:
            if is_routable:
                ip_type = "Public"
            else:
                ip_type = "Private"
        clint_ip = "103.230.106.25"
        url = "http://ip-api.com/json/" + clint_ip
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        try:
            my_ip = IpStore.objects.get(ip_name=clint_ip)
        except Exception as e:
            try:
                IpStore.objects.create(
                    ip_name=clint_ip,
                    ip_type=ip_type,
                    city=data['city'],
                    region=data['regionName'],
                    country=data['country'],
                    lat=data['lat'],
                    lon=data['lon'],
                    timezone=data['timezone'],
                    zip_code=data['zip'],
                    isp=data['isp'],
                    org=data['org'],
                    query=data['query'],
                    status=data['status'],
                    ass=data['as'],
                    countryCode=data['countryCode']
                )
            except Exception as e:
                IpStore.objects.create(
                    ip_name=clint_ip,
                    ip_type=ip_type,
                    city="Unknown",
                    region="Unknown",
                    country="Unknown",
                    lat="Unknown",
                    lon="Unknown",
                    timezone="Unknown",
                    zip_code="Unknown",
                    isp="Unknown",
                    org="Unknown",
                    query="Unknown",
                    status="Unknown",
                    ass="Unknown",
                    countryCode="Unknown"
                )

            my_ip = IpStore.objects.get(ip_name=clint_ip)
        context['ip_address'] = my_ip
        return context


class BlogCommentLikeView(TemplateView):
    model = BlogComment

    def get(self, request, *args, **kwargs):
        comment_id = self.kwargs['comment_id']
        comment = self.model.objects.get(id=comment_id)
        comment.like += 1
        comment.save()
        return redirect('/blog/post/' + str(comment.blog_post.id))


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
            replay_comment = None
            replay = None
        try:
            clint_ip, is_routable = get_client_ip(self.request)
            comment_id = int(request.POST.get('comment_id'))
            cmt_lik = get_object_or_404(BlogComment, pk=comment_id)
            # cmt_lik.like.add('20')
            comment = BlogComment.objects.get(pk=comment_id)
            comment.total_like += 1
            comment.save()
            return redirect('blog_details', pk=pk)
        except Exception as e:
            comment = None
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.post = object
            user.parent = replay
            user.save()
            return redirect('blog_details', pk=pk)
        return render(request, self.template_name)
