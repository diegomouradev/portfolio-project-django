import os
from django.conf import settings
from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '%s' % (self.name)

def images_path():
    return os.path.join(settings.STATIC_URL, 'img')

class Post(models.Model):
    title = models.CharField(max_length=80)
    sub_title = models.CharField(max_length=150)
    image = models.FilePathField(path=images_path, default="img")
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    categories = models.ManyToManyField('Category', related_name='posts')
    author = models.CharField(max_length=60)

    def __str__(self):
        return '%s' % (self.title)


class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
