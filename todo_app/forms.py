from django import forms

from todo_app.models import Task


class FirstForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class TaskForm(forms.ModelForm):
    # deadline_2 = forms.DateTimeField()
    class Meta:
        model = Task
        fields = "__all__"
        # exclude = ["title"]
        widgets = {
            "deadline": forms.DateTimeInput(attrs={}),
            "description": forms.Textarea(attrs={"rows": 1, "cols": 10})
        }
