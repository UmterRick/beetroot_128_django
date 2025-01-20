from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, TemplateView

from accounts.forms import UserRegisterForm


# Create your views here.
class UserRegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = "accounts_templates/register.html"
    success_url = reverse_lazy("user-login")

    def form_valid(self, form):
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get("password"))
        user.save()
        return redirect(self.success_url)


class UserLoginView(LoginView):
    template_name = "accounts_templates/login.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy("user-profile")


@method_decorator(login_required, name="dispatch")
class UserProfileView(TemplateView):
    template_name = "accounts_templates/profile.html"




