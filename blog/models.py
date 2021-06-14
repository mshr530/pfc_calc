from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# CATEGORY = (('breakfast','朝食'),('lunch','昼食'),('dinner','夕食'))
class Blog(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
  title = models.CharField(max_length=200)
  content = models.TextField()
  # category = models.CharField(max_length=200, choices=CATEGORY)
  created = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.title

