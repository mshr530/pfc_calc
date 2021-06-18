from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

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

class BlogCreate(LoginRequiredMixin, CreateView):
  model = Blog
  template_name = 'blog/create.html'
  fields = ['title', 'content']
  success_url = reverse_lazy('blogs')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(BlogCreate, self).form_valid(form)

class BlogUpdate(LoginRequiredMixin, UpdateView):
  model = Blog
  template_name = 'blog/update.html'
  fields = ['title', 'content']
  success_url = reverse_lazy('blogs')


class BlogDelete(LoginRequiredMixin, DeleteView):
  template_name = 'blog/delete.html'
  model = Blog
  context_object_name = 'blog'
  success_url = reverse_lazy('blogs')
  
def search(request):
  return render(request, 'blog/search.html')
