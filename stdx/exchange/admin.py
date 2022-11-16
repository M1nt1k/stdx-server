from django.contrib import admin

from .models import *

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(Owner)
admin.site.register(University)
admin.site.register(Files)