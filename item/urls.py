
from django.urls import path

from . import views

urlpatterns = [
    # item
    path('', views.item),
    # create_item
    path('create_item', views.create_item),
    # my checkout
    path('my_bids', views.my_bids),
    # make a bid
    path('make_bid', views.make_bid),

]