from datetime import datetime

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from todo_app.models import Task


# Create your tests here.
class SomeTestCase(TestCase):
    def setUp(self):
        User(username="TestUser").save()
        test_tasks = [
            Task(**{
                "title": "TestTask1",
                "assign_to": User.objects.first(),
                "description": "Test desc",
                "priority_level": 3,
                "deadline": datetime(2025, 1, 1, 12, 0, 0),
                "created_at": datetime(2024, 12, 31, 12, 0, 0),
            }),
            Task(**{
                "title": "TestTask2",
                "assign_to": User.objects.first(),

                "description": "Test desc 2",
                "priority_level": 1,
                "deadline": datetime(2025, 1, 1, 12, 0, 0),
                "created_at": datetime(2024, 12, 31, 12, 0, 0),
            }),
            Task(**{
                "title": "TestTask3",
                "assign_to": User.objects.first(),
                "description": "Test desc 3",
                "priority_level": 4,
                "deadline": datetime(2025, 1, 1, 12, 0, 0),
                "created_at": datetime(2024, 12, 31, 12, 0, 0),
            })
        ]
        Task.objects.bulk_create(test_tasks)

    def test_task_above_priority_level(self):
        priority_level = 2
        important_tasks = Task.above_priority_level(priority_level)
        print(important_tasks)
        self.assertIs(len(important_tasks), 2)


    def test_request(self):
        response = self.client.get(reverse("task-list-new"))
        self.assertIs(len(response.context["tasks"]), 3)
