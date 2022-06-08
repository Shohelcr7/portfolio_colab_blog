from django.urls import path
from . import views


app_name ='blog'

urlpatterns = [
path('',views.BlogList.as_view() , name = 'blog_list'),
path('create/',views.CreateBlog.as_view() , name = 'blog_create'),
path('details/<pk>/',views.blog_details , name = 'details'),
path('liked/<pk>/', views.liked, name='blog_liked'),
path('loved/<pk>/', views.loved, name='blog_loved'),
path('unliked/<pk>/', views.unliked, name='blog_unliked'),
path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
path('edit/<pk>/', views.UpdateBlog.as_view(), name='blog_edit'),
#path('create',views.CreateBlog.as_view() , name = 'blog_create'),




]
