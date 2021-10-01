from django.http import request
from ipware import get_client_ip
import json, urllib
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, DetailView
from .models import BlogPost, BlogComment, IpStore
from .forms import CommentForm

# def visitor_ip_address(request):
#     return request.META.get(
#         'HTTP_X_FORWARDED_FOR', request.META.get('REMOTE_ADDR', '')
#     ).split(',')[0].strip()


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
        # visitor_ip = visitor_ip_address(self.request)
        # try:
        #     ip_name = IpStore.objects.get(ip_name=visitor_ip)
        # except Exception as e:
        #     IpStore.objects.create(ip_name=visitor_ip)
        #     ip_name = IpStore.objects.get(ip_name=visitor_ip)
        # context['visitor_ip'] = ip_name
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
        print(data)
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
        print(clint_ip, ip_type, "------------------",data)
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
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.post = object
            user.parent = replay
            user.save()
            return redirect('blog_details', pk=pk)
        return render(request, self.template_name)
