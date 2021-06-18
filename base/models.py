from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
CATEGORY = (('朝食','朝食'),('昼食','昼食'), ('夕食','夕食'),('間食','間食'))
class Food(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  category = models.CharField(max_length=200, choices=CATEGORY)
  name = models.CharField(max_length=200)
  kcal = models.PositiveSmallIntegerField()
  protein = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)])
  fat = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)])
  carb = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)])
  description = models.TextField(null=True, blank=True)
  eaten_date = models.DateField(editable=True, blank=True, null=True)
  created = models.DateTimeField(auto_now_add=True)
  def __str__(self):
      return self.name

class Target(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  kcal = models.PositiveSmallIntegerField()
  protein = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)])
  fat = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)])
  carb = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True, default=0.0, validators=[MaxValueValidator(999.9), MinValueValidator(0.0)])
  created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
  # 以下はadminページでの表示、正味いらん、あとエラーになる
  # def __str__(self):
  #   return self.user