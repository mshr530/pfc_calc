from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy


# Create your views here.
def index(request):
  blogs = Blog.objects.all()

  context = {
    'blogs' : blogs
  }
  return render(request, 'blog/blogs.html', context)

def blog(request, pk):
  blog = get_object_or_404(Blog, pk=pk)
  
  context = {
    'blog': blog
  }
  return render(request, 'blog/blog.html', context)

class BlogCreate(CreateView):
  model = Blog
  template_name = 'blog/create.html'
  fields = '__all__'
  success_url = reverse_lazy('blogs')

class BlogUpdate(UpdateView):
  model = Blog
  template_name = 'blog/update.html'
  fields = '__all__'
  success_url = reverse_lazy('blogs')

class BlogDelete(DeleteView):
  template_name = 'base/delete.html'
  model = Blog
  context_object_name = 'blog'
  success_url = reverse_lazy('blogs')
  
def search(request):
  return render(request, 'blog/search.html')
