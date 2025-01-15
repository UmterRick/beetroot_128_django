from datetime import datetime, timezone

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from todo_app.forms import FirstForm, TaskForm
from todo_app.models import Task


# Create your views here.
def greetings(request):
    return render(request, "todo_app_templates/index.html")


def all_tasks(request):
    if request.method == "GET":
        query = Task.objects.select_related("assign_to")
        return render(request, "todo_app_templates/tasks.html",
                      context={
                          "tasks": query,
                          "dt_now": datetime.now(tz=timezone.utc),
                          "task_form": TaskForm
                      })
    elif request.method == "POST":
        print(request)
        form = TaskForm(request.POST)
        if form.is_valid():
            print("Form is valid")
            new_task = form.save(commit=False)
            new_task.save()


        return redirect("tasks-list")


def handle_form(request):
    if request.method == "GET":
        return render(request, "todo_app_templates/form.html",
                      context={"my_form": FirstForm}
                      )
    elif request.method == "POST":
        print("Login User")
        return redirect("tasks-list")



class TaskListView(ListView):
    model = Task
    template_name = "todo_app_templates/tasks.html"
    context_object_name = "tasks"


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_app_templates/task_create.html"
    success_url = reverse_lazy("task_list")


class TaskDetailsView(DetailView):
    model = Task
    template_name = "todo_app_templates/task_details.html"
    context_object_name = "task"


class TaskEditView(UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "todo_app_templates/task_create.html"
    success_url = reverse_lazy("task_list")


class TaskDeleteView(DeleteView):
    model = Task
    template_name = "todo_app_templates/task_delete.html"
    success_url = reverse_lazy("task_list")
