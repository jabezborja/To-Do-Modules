from django.contrib import admin
from .models import Task, TaskNote

admin.site.register(Task)
admin.site.register(TaskNote)
