from django.shortcuts import get_object_or_404, render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Blog
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
  today = datetime.today()
  blogs = Blog.objects.order_by('-updated').filter(is_public='公開')[:50]
  count = Blog.objects.order_by('-updated').filter(updated__date=today).count()
  context = {
    'blogs': blogs,
    'count': count
  }
  return render(request, 'blog/latest_blogs.html', context)

def blog(request, pk):
  blog = get_object_or_404(Blog, pk=pk)
  if blog.link_1 is not None and blog.link_2 is not None:
    link_1 = blog.link_1
    link_2 = blog.link_2
    context = {
      'blog': blog,
      'link_1': link_1,
      'link_2': link_2,
    }
  elif blog.link_1 is not None or blog.link_2 is not None:
    link_1 = blog.link_1
    link_2 = blog.link_2
    context = {
      'blog': blog,
      'link_1': link_1,
      'link_2': link_2,
    }
  else:
    context = {
      'blog': blog,
    }
  print(blog.link_2)

  return render(request, 'blog/blog.html', context)

class BlogCreate(LoginRequiredMixin, CreateView):
  model = Blog
  template_name = 'blog/create.html'
  fields = ['title', 'content','link_1', 'link_2', 'is_public']
  success_url = reverse_lazy('latest_blogs')

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(BlogCreate, self).form_valid(form)

class BlogUpdate(LoginRequiredMixin, UpdateView):
  model = Blog
  template_name = 'blog/update.html'
  fields = ['title', 'content', 'link_1', 'link_2', 'is_public']
  success_url = reverse_lazy('latest_blogs')


class BlogDelete(LoginRequiredMixin, DeleteView):
  template_name = 'blog/delete.html'
  model = Blog
  context_object_name = 'blog'
  success_url = reverse_lazy('latest_blogs')


class BlogList(LoginRequiredMixin, ListView):
  model = Blog
  template_name = 'blog/all_blogs.html'
  context_object_name = 'blogs'
  ordering = ['-created']
  paginate_by = 20

def blog_search_results(request):
  queryset_list = Blog.objects.order_by('-created')
  
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      # queryset_list = queryset_list.filter(Q(user__icontains=keywords)|Q(created__icontains=keywords)|Q(title__icontains=keywords))
      queryset_list = queryset_list.filter(
        # Q(user__icontains=keywords)|
        Q(created__icontains=keywords)|
        Q(title__icontains=keywords)
      )
  
  context = {
    'blogs': queryset_list
  }

  return render(request, 'blog/blog_search_results.html', context)