from django.contrib import admin
from .models import Task, University, Category, File


admin.site.register(Task)
admin.site.register(University)
admin.site.register(Category)
admin.site.register(File)