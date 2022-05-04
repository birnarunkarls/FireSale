from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page),
    # category
    path('category', views.category),
    # about
    path('about', views.about),

]
