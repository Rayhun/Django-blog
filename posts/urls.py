from django.urls import path
# from .views import post_create,post_detale,post_list,post_update,post_delete

from . import views

urlpatterns = [
    path('', views.post_home, name = "post_home"),
    path('create/', views.post_create, name = "post_create"),
    path('single/<int:pk>', views.post_detale, name = "post_detail"),
    path('list/<int:pk>', views.post_list, name = "post_list"),
    path('update/<int:pk>', views.post_update, name = "post_update"),
    path('delete/<int:pk>', views.post_delete, name = "post_delete"),
]
