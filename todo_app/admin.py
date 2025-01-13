from django.contrib import admin
from django.contrib.admin import register

from todo_app.models import Task


# Register your models here.
@register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("title", "deadline", "assign_to")