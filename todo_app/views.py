from datetime import datetime, timezone

from django.shortcuts import render

from todo_app.models import Task


# Create your views here.
def greetings(request):
    return render(request, "todo_app_templates/index.html")


def all_tasks(request):
    query = Task.objects.select_related("assign_to")
    return render(request, "todo_app_templates/tasks.html",
                  context={
                      "tasks": query, "dt_now": datetime.now(tz=timezone.utc)
                  })