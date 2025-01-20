from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from django import forms

from todo_app.models import Task


class FirstForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-control'
        self.helper.layout = Layout(
            Row(
                Column('login', css_class='form-control form-control-lg')
            ),
            Row(
                Column('password', css_class='form-control')
            ),
            Submit('submit', "Login",  css_class="btn btn-success")
        )

    login = forms.CharField(max_length=100, label="Your Username")
    password = forms.CharField(widget=forms.PasswordInput, label="Your Password")



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



