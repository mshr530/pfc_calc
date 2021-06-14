from django.urls import path 
from . import views
from .views import BlogCreate, BlogUpdate, BlogDelete
# blogs
urlpatterns = [
  path('', views.index, name='blogs'),
  path('blog/<int:pk>/', views.blog, name='blog'),
  path('create/', BlogCreate.as_view(), name='blog-create'),
  path('update/<int:pk>/', BlogUpdate.as_view(), name='blog-update'),
  path('delete/<int:pk>/', BlogDelete.as_view(), name='blog-delete'),
  path('search/', views.search, name='blog-search'),
]