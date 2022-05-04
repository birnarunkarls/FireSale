
from django.urls import path

from . import views

urlpatterns = [
    # register
    path('register', views.register),
    # login
    path('login', views.login),
    # profile - þurfum að laga
    path('', views.profile),
    path('profile_edit', views.profile_edit),
]