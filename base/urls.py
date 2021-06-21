from django.urls import path
from .views import FoodCreate, FoodUpdate, FoodDelete, FoodList, CustomLoginView, RegisterPage, TargetCreate
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
  path('login', CustomLoginView.as_view(), name='login'),
  path('logout', LogoutView.as_view(next_page='login'), name='logout'),
  path('register', RegisterPage.as_view(), name='register'),

  path('', views.foods, name='today_foods'),
  path('all_foods', FoodList.as_view(), name='all_foods'),
  path('all_foods/food_search_results/', views.food_search_results, name='food_search_results'),
  path('target', TargetCreate.as_view(), name='target'),
  # path('', FoodList.as_view(), name='foods'),
  path('create/', FoodCreate.as_view(), name='food-create'),
  path('update/<int:pk>', FoodUpdate.as_view(), name='food-update'),
  path('delete/<int:pk>', FoodDelete.as_view(), name='food-delete'),
  path('user_page/<int:pk>', views.user_page, name='user_page'),
]