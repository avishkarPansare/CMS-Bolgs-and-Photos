from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# Blog category model which stored the category of blog
class Blog_Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name

# Blog is stored the all blog deatils


class Blog(models.Model):
    Title = models.CharField(max_length=50)
    Category = models.ForeignKey(Blog_Category, on_delete=models.CASCADE)
    Oneline = models.CharField(max_length=100)
    Content = models.TextField()
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

# Photo category is stored the photo category


class Photo_Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    photo = models.ImageField(null=False, blank=False)
    description = models.TextField()
    category = models.ForeignKey(Photo_Category, on_delete=models.CASCADE)
    Date = models.DateField(auto_now_add=True)
    Time = models.TimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
