from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page, name="fire_sale-home_page"),
    # category
    path('category', views.category, name="fire_sale-category"),
    # about
    path('about', views.about, name="fire_sale-about"),

]
