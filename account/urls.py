from django.urls import path
# from .views import CustomLoginView, RegisterPage
# from django.contrib.auth.views import LogoutView
from . import views
urlpatterns = [
  # path('login', CustomLoginView.as_view(), name='login'),
  # path('logout', LogoutView.as_view(next_page='login'), name='logout'),
  # path('register', RegisterPage.as_view(), name='register'),
  # path('dashboard/<int:pk>', views.dashboard, name='dashboard'),
  path('register', views.register, name='register'),
  path('login', views.login, name='login'),
  path('logout', views.logout, name='logout'),
  path('dashboard/<int:pk>', views.dashboard, name='dashboard'),
] 