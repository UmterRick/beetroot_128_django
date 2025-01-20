from django.contrib.auth.views import LogoutView
from django.urls import path
from accounts import views

urlpatterns = [
    path('register/', views.UserRegisterView.as_view(), name="user-register"),
    path('login/', views.UserLoginView.as_view(), name="user-login"),
    path('profile/', views.UserProfileView.as_view(), name="user-profile"),
    path('logout/', LogoutView.as_view(), name="user-logout"),
]