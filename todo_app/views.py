from datetime import datetime, timezone

from django.http import HttpResponse
from django.shortcuts import render
from todo_app.models import Task

# Create your views here.
def greetings(request):
    return render(request, "todo_app_templates/index.html")


def all_tasks(request):
    return render(request, "todo_app_templates/tasks.html",
                  context={
                      "tasks": Task.objects.all(), "dt_now": datetime.now(tz=timezone.utc)
                  })