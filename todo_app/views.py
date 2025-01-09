from pyexpat.errors import messages

from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task

# Create your views here.
def greetings(request):
    print(request)
    return HttpResponse("<h2>Hello from Django :)</h2>")


def all_tasks(request):
    tasks = Task.objects.all()
    msg = "<h2>"
    for task in tasks:
        msg += f"title: {task.title} <br>"
        msg += f"assign: {task.assign_to} <br>"
        msg += f"deadline: {task.deadline} <br>"
    msg += "</h2>"
    return HttpResponse(msg)