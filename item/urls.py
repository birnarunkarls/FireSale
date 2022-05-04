
from django.urls import path

from . import views

urlpatterns = [
    # item
    path('', views.item),
    # create_item
    path('create_item', views.create_item),

]