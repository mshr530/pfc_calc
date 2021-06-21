from django.contrib import admin
from .models import Blog
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'user', 'is_public')
  list_display_links = ('id',)
  list_filter = ('user', 'is_public')
  search_fields = ('title',)
  list_per_page = 50
admin.site.register(Blog, BlogAdmin)