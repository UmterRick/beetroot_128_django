from todo_app.models import Task

Task.objects.all()
Task.objects.all().order_by("-deadline")
Task.objects.filter(title="Task 1")
Task.objects.filter(title__exact="Task 1")
Task.objects.filter(title__iexact="task 1")
Task.objects.filter(title__contains="task")
Task.objects.filter(title__icontains="task")
Task.objects.filter(assign_to=1)
Task.objects.filter(assign_to__email__icontains="com")


Task.objects.all().values_list("id")
Task.objects.all().values_list("title")
Task.objects.all().values_list("title", flat=True)
