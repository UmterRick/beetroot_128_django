from django.urls import path

from todo_app.views import TaskListView, TaskCreateView, TaskDetailsView, TaskEditView, TaskDeleteView

urlpatterns = [
    path('', TaskListView.as_view(), name="task-list-new"),
    path('create/', TaskCreateView.as_view(), name="task-create"),
    path('<int:pk>', TaskDetailsView.as_view(), name="task-details"),
    path('<int:pk>/update/', TaskEditView.as_view(), name="task-edit"),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name="task-delete"),
]