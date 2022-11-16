from django.db import models

def user_path(instance, filename):
    return f'{instance.own.vk_id}/{filename}'

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    files = models.ForeignKey(
        'Files',
        on_delete = models.PROTECT,
        null = True
    )
    taskType = models.ForeignKey(
        'Category',
        on_delete = models.PROTECT,
        null = True
    )
    universityTitle = models.ForeignKey(
        'University',
        on_delete = models.PROTECT,
        db_index = True,
        null = True
    )
    orderDate = models.DateTimeField(
        auto_now_add=True
    )
    deliveryDate = models.DateTimeField(auto_now=False)
    price = models.IntegerField(
        default=100
    )
    is_published = models.BooleanField(default=True)
    own = models.ForeignKey(
        'Owner',
        verbose_name='Owner',
        on_delete = models.CASCADE
    )

    def __str__(self):
        return self.title

class Files(models.Model):
    name = models.CharField(
        max_length = 255,
        default = 'No Title'
    )
    filesUrl = models.FileField(
        upload_to = 'data',
        null=True,
        max_length=255
    )

    def __str__(self):
        return self.name

class University(models.Model):
    name = models.CharField(
        max_length = 255,
        db_index = True
    )

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(
        max_length = 100,
        db_index = True
    )

    def __str__(self):
        return self.name

class Owner(models.Model):
    vk_id = models.CharField(
        max_length = 10,
        db_index = True
    )

    def __str__(self):
        return self.vk_id
