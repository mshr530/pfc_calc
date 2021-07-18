from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import date
# Create your models here.
FOOD_CATEGORY = (('朝食','朝食'),('昼食','昼食'), ('夕食','夕食'),('間食','間食'))
class Food(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='ユーザー')
  category = models.CharField(max_length=200, choices=FOOD_CATEGORY, verbose_name='カテゴリー')
  name = models.CharField(max_length=200, verbose_name='名前')
  kcal = models.PositiveSmallIntegerField(verbose_name='カロリー')
  protein = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='タンパク質')
  fat = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='脂質')
  carb = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='炭水化物')
  eaten_date = models.DateField(verbose_name='食べた日付', default=date.today, help_text='※yyyy-mm-dd')
  created = models.DateTimeField(auto_now_add=True, verbose_name='作成日')
  def __str__(self):
      return self.name

class Target(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='ユーザー')
  kcal = models.PositiveSmallIntegerField(verbose_name='カロリー')
  protein = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='タンパク質')
  fat = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='脂質')
  carb = models.DecimalField(max_digits=4, decimal_places=1, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='炭水化物')
  created = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name='作成日')
  # 以下はadminページでの表示、正味いらん、あとエラーになる
  # def __str__(self):
  #   return self.user

class Favorite(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='user')
  category = models.CharField(max_length=200, choices=FOOD_CATEGORY, verbose_name='category')
  name = models.CharField(max_length=200, verbose_name='name')
  kcal = models.PositiveSmallIntegerField(verbose_name='kcal')
  protein = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='protein')
  fat = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='fat')
  carb = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)], verbose_name='carb')
  created = models.DateTimeField(auto_now_add=True, verbose_name='created')
  def __str__(self):
      return self.name