from django.db import models
from os import path
from django.conf import settings

def upload_to(instance, filename):
    return path.join(instance.task.title, filename)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    orderDate = models.DateTimeField(auto_now_add=True)
    university = models.ForeignKey('University', related_name='tasks', on_delete=models.DO_NOTHING)
    category = models.ForeignKey('Category', related_name='tasks', on_delete=models.DO_NOTHING)
    deliveryDate = models.DateTimeField(auto_now=False)
    price = models.IntegerField(default=100)
    is_published = models.BooleanField(default=True)
    owner = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class University(models.Model):
    name = models.CharField(
        max_length = 255,
        db_index = True
    )
    # task = models.ForeignKey('Task', related_name='university', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length = 255,
        db_index = True
    )
    # task = models.ForeignKey('Task', related_name='category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class File(models.Model):
    name = models.CharField(max_length=200, default=None)
    file = models.FileField(blank=True, upload_to=upload_to, default='')
    task = models.ForeignKey('Task', related_name='files', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Responses(models.Model):
    owner = models.ForeignKey('auth.User', related_name='responces', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    about = models.TextField(blank=False)
    price = models.IntegerField(default=100)
    deliveryDate = models.DateTimeField(auto_now=False) 
    task = models.ForeignKey('Task', related_name='responces', on_delete=models.CASCADE)
