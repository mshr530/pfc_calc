from django.db import models
from django.contrib.auth.models import User

# Create your models here.
BLOG_IS_PUBLIC = (('公開','公開'),('非公開','非公開'))
class Blog(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='ユーザー')
  title = models.CharField(max_length=200, verbose_name='タイトル')
  content = models.TextField(verbose_name='コンテンツ')
  link_1 = models.URLField(verbose_name='参考文献リンク1', max_length=300, null=True, blank=True)
  link_2 = models.URLField(verbose_name='参考文献リンク2', max_length=300, null=True, blank=True)
  # category = models.CharField(max_length=200, choices=CATEGORY)
  is_public = models.CharField(max_length=200, choices=BLOG_IS_PUBLIC, verbose_name='公開設定', default='公開')
  created = models.DateTimeField(auto_now=True, verbose_name='作成日')
  updated = models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.title

