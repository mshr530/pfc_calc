from django.urls import path
from .views import FoodCreate, FoodUpdate, FoodDelete
from . import views
urlpatterns = [
  path('', views.foods, name='foods'),
  # path('', FoodList.as_view(), name='foods'),
  path('create', FoodCreate.as_view(), name='create'),
  path('update/<int:pk>', FoodUpdate.as_view(), name='update'),
  path('delete/<int:pk>', FoodDelete.as_view(), name='delete'),
]