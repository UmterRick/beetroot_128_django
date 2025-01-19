from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(null=False, unique=True)
    assign_to = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    priority_level = models.IntegerField(validators=[MaxValueValidator(5), MinValueValidator(1)], default=3)
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now=True)

    @classmethod
    def above_priority_level(cls, level):
        return cls.objects.filter(priority_level__gt=level)