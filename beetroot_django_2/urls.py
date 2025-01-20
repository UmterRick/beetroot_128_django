"""
URL configuration for beetroot_django_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib import admin
from django.urls import path, include
from todo_app import views, urls as todo_urls
from accounts import urls as account_urls
urlpatterns = [
    # path('first-url/', views.greetings),
    # path('tasks/', views.all_tasks, name="tasks-list"),
    # path('tasks-generic/', views.TaskListView.as_view(), name="tasks-generic-list"),
    # path('form/', views.handle_form, name="test-form"),
    path('admin/', admin.site.urls),
    path('tasks/', include(todo_urls.urlpatterns)),
    path('auth/', include(account_urls.urlpatterns)),
] +  debug_toolbar_urls()
