from django.urls import path
from . import views

urlpatterns = [
    path('user/create/', views.UserCreateView.as_view(), name='user_create'),
    path('', views.BlogHomePageView.as_view(), name='blog_home'),
    path(
        'details/<int:pk>/', views.BlogDetails.as_view(), name='blog_details'
    ),
    path('blog/search/', views.SearchView.as_view(), name='blog_search'),
]
