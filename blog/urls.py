from django.urls import path 
from . import views
from .views import BlogCreate, BlogUpdate, BlogDelete, BlogList
# blogs
urlpatterns = [
  path('', views.index, name='latest_blogs'),
  path('blog/<int:pk>/', views.blog, name='blog'),
  path('create/', BlogCreate.as_view(), name='blog-create'),
  path('update/<int:pk>/', BlogUpdate.as_view(), name='blog-update'),
  path('delete/<int:pk>/', BlogDelete.as_view(), name='blog-delete'),
  path('all_blogs/', BlogList.as_view(), name='all_blogs'),
  path('all_blogs/blog_search_results/', views.blog_search_results, name='blog_search_results'),
]