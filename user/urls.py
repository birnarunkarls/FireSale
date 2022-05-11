from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from . import views

urlpatterns = [
    # register
    path('register', views.register, name="user-register"),
    # login
    path('login', LoginView.as_view(template_name='user/login.html'), name="user-login"),
    # log out
    path('logout', LogoutView.as_view(next_page='user-login'), name="user-logout"),
    # profile - þurfum að laga
    path('', views.profile, name="user-profile"),
    path('profile_edit', views.profile_edit, name="user-profile_edit")
]