from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(null=False, unique=True)
    assign_to = models.CharField()
    description = models.TextField()
    priority_level = models.SmallIntegerField(max_length=5),
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)
