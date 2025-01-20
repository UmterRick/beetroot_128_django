from django import forms
from django.contrib.auth.models import User


class UserRegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    verify_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]


    def clean_verify_password(self):
        password = self.cleaned_data.get("password")
        verify_password = self.cleaned_data.get("verify_password")

        if password != verify_password:
            raise forms.ValidationError("Passwords fo not match!")
        return verify_password
