import os
from django.conf import settings
from django.db import models

# Create your models here.


def images_path():
    return os.path.join(settings.STATIC_URL, 'img')


class Projects(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=100)
    image = models.FilePathField(path=images_path)

    def __str__(self):
        return '%s' % (self.title)
