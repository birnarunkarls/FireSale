
from django.urls import path

from . import views

urlpatterns = [
    # register
    path('register', views.register, name="user-register"),
    # login
    path('login', views.login, name="user-login"),
    # profile - þurfum að laga
    path('', views.profile, name="user-profile"),
    path('profile_edit', views.profile_edit, name="user-profile_edit"),
]