from django.urls import path
from . import views

urlpatterns = [
    path('', views.BlogHomePageView.as_view(), name='blog_home'),
    path(
        'details/<int:pk>/', views.BlogDetails.as_view(), name='blog_details'
    ),
]
