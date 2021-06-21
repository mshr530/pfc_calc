from django.shortcuts import get_object_or_404, render, redirect
from .models import Food, Target
from blog.models import Blog
from django.contrib.auth.models import User
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
# function-based view 用のアクセス制限
from django.contrib.auth.decorators import login_required
import datetime
from django.db.models import Sum, Q


class CustomLoginView(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  # すでにログインしてるのにアクセスするとリダイレクトする
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('today_foods')

class RegisterPage(FormView):
  template_name = 'base/register.html'
  form_class = UserCreationForm
  redirect_authenticated_user = True
  success_url = reverse_lazy('today')

  def form_valid(self, form):
    user = form.save()
    if user is not None:
      login(self.request, user)
    return super(RegisterPage, self).form_valid(form)

  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated:
      return redirect('today_foods')
    return super(RegisterPage, self).get(*args, **kwargs)




class FoodList(LoginRequiredMixin, ListView):
  model = Food
  template_name = 'base/all_foods.html'
  context_object_name = 'foods'
  ordering = ['-created']
  paginate_by = 20
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   # context内の名前で左の値がhtml上で使えるようになる
  #   context['color'] = 'red'
  #   context['foods'] = context['foods'].filter(user=self.request.user)

  #   search_input = self.request.GET.get('search-area') or ''
  #   if search_input:
  #     context['foods'] = context['foods'].filter(Q(name__icontains=search_input)|Q(category__icontains=search_input))
  #   context['search_input'] = search_input
  #   return context



@login_required
def foods(request):
  today = datetime.datetime.today()
  # foods = Food.objects.filter(eaten_date=today)
  user_foods = Food.objects.order_by('-category').filter(user=request.user, eaten_date=today)
  try:
    target = Target.objects.latest('created')
  except Target.DoesNotExist:
    target = None

  user_breakfast_list = user_foods.filter(category='朝食')
  user_lunch_list = user_foods.filter(category='昼食')
  user_snack_list = user_foods.filter(category='間食')
  user_dinner_list = user_foods.filter(category='夕食')
  # これでも合計カロリーは出る
  # kcal = foods.aggregate(Sum('kcal'))
  # protein = foods.aggregate(Sum('protein'))

  # total_kcal
  kcal_list = [food['kcal'] for food in user_foods.values('kcal')]
  ttl_kcal = sum(kcal_list)
    # total_protein
  protein_list = [food['protein'] for food in user_foods.values('protein')]
  ttl_protein = sum(protein_list)
    # total_fat
  fat_list = [food['fat'] for food in user_foods.values('fat')]
  ttl_fat = sum(fat_list)
    # total_carb
  carb_list = [food['carb'] for food in user_foods.values('carb')]
  ttl_carb = sum(carb_list)
  
  context = {
    'ttl_kcal': ttl_kcal,
    'ttl_protein': ttl_protein,
    'ttl_fat': ttl_fat,
    'ttl_carb': ttl_carb,
    'user_foods': user_foods,
    'user_breakfast_list': user_breakfast_list,
    'user_lunch_list': user_lunch_list,
    'user_dinner_list': user_dinner_list,
    'user_snack_list': user_snack_list,
    'target': target,
  }
  return render(request, 'base/today_foods.html', context)


class TargetCreate(LoginRequiredMixin, CreateView):
  template_name = 'base/target.html'
  model = Target
  fields = '__all__'
  success_url = reverse_lazy('today_foods')
  context_object_name = 'targets'
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    # context内の名前で左の値がhtml上で使えるようになる
    context['target'] = Target.objects.latest('created')
    return context
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super(TargetCreate, self).form_valid(form)


class FoodCreate(LoginRequiredMixin, CreateView):
  template_name = 'base/create.html'
  model = Food
  fields = ['category','name', 'kcal', 'protein', 'fat', 'carb']
  success_url = reverse_lazy('today_foods')
  
  def form_valid(self, form):
    form.instance.user = self.request.user
    form.instance.eaten_date = datetime.datetime.now().strftime('%Y-%m-%d')
    return super(FoodCreate, self).form_valid(form)



class FoodUpdate(LoginRequiredMixin, UpdateView):
  template_name = 'base/update.html'
  model = Food 
  fields = ['category','name', 'kcal', 'protein', 'fat', 'carb']
  success_url = reverse_lazy('today_foods')



class FoodDelete(LoginRequiredMixin, DeleteView):
  template_name = 'base/delete.html'
  model = Food 
  context_object_name = 'food'
  success_url = reverse_lazy('today_foods')

def user_page(request, pk):
  user = get_object_or_404(User, pk=pk)
  user_blogs = Blog.objects.order_by('-created').filter(user=request.user)[:5]
  today = datetime.datetime.today()
  # foods = Food.objects.filter(eaten_date=today)
  today_user_foods = Food.objects.order_by('-category').filter(user=request.user, eaten_date=today)
  
  context = {
    'user': user,
    'today_user_foods': today_user_foods,
    'user_blogs': user_blogs,
  }
  print(user_blogs)
  return render(request, 'base/user_page.html', context)

def food_search_results(request):
  queryset_list = Food.objects.order_by('-created')
  
  if 'keywords' in request.GET:
    keywords = request.GET['keywords']
    if keywords:
      queryset_list = queryset_list.filter(Q(name__icontains=keywords)|Q(category__icontains=keywords)|Q(eaten_date__icontains=keywords))
  
  context = {
    'foods': queryset_list
  }

  return render(request, 'base/food_search_results.html', context)