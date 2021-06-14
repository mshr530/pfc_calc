from django.shortcuts import render
from .models import Food
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
  template_name = 'base/login.html'
  fields = '__all__'
  redirect_authenticated_user = True

  def get_success_url(self):
    return reverse_lazy('foods')

class FoodList(ListView):
  model = Food
  template_name = 'base/all_foods.html'
  context_object_name = 'foods'
  ordering = ['-created']

import datetime
from django.db.models import Sum
def foods(request):
  today = datetime.datetime.today()
  foods = Food.objects.filter(eaten_date=today)
  # これでも合計カロリーは出る
  # kcal = foods.aggregate(Sum('kcal'))
  # protein = foods.aggregate(Sum('protein'))

  # total_kcal
  kcal_list = [food['kcal'] for food in foods.values('kcal')]
  ttl_kcal = sum(kcal_list)
    # total_protein
  protein_list = [food['protein'] for food in foods.values('protein')]
  ttl_protein = sum(protein_list)
    # total_fat
  fat_list = [food['fat'] for food in foods.values('fat')]
  ttl_fat = sum(fat_list)
    # total_carb
  carb_list = [food['carb'] for food in foods.values('carb')]
  ttl_carb = sum(carb_list)
  
  context = {
    'foods': foods,
    'ttl_kcal': ttl_kcal,
    'ttl_protein': ttl_protein,
    'ttl_fat': ttl_fat,
    'ttl_carb': ttl_carb,
  }
  return render(request, 'base/foods.html', context)

# class FoodList(ListView):
#   model = Food
#   template_name = 'base/foods.html'
#   # html内で使う変数名をobject_listから任意名に変更
#   context_object_name = 'foods'
#   def get_context_data(self, **kwargs):
#     context = super().get_context_data(**kwargs)
#     context['foods'] = [food['kcal'] for food in Food.objects.values('kcal')]
#     context['total_total'] = sum(context['foods'])
#     return context
  # def get_context_data(self, **kwargs):
  #   context = super().get_context_data(**kwargs)
  #   context['food'] = 'pancake'
  #   return context

class FoodCreate(CreateView):
  template_name = 'base/create.html'
  model = Food
  fields = '__all__'
  success_url = reverse_lazy('foods')


class FoodUpdate(UpdateView):
  template_name = 'base/update.html'
  model = Food 
  fields = '__all__'
  success_url = reverse_lazy('foods')

class FoodDelete(DeleteView):
  template_name = 'base/delete.html'
  model = Food 
  context_object_name = 'food'
  success_url = reverse_lazy('foods')
