from django.contrib import admin
from .models import Blog, Blog_Category, Photo, Photo_Category
# Register your models here.


@admin.register(Blog_Category)
class Blog_CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Blog)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['Title', 'Category', 'Oneline',
                    'Content', 'Date', 'Time', 'user']


@admin.register(Photo_Category)
class Photo_CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Photo)
class PhotoModelAdmin(admin.ModelAdmin):
    list_display = ['photo', 'description', 'category', 'Date', 'Time', 'user']
