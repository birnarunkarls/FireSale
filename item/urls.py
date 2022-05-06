
from django.urls import path

from . import views

urlpatterns = [
    # item
    path('', views.item, name="item-item"),
    # create_item
    path('create_item', views.create_item, name="item-create_item"),
    # my checkout
    path('my_bids', views.my_bids, name="item-my_bids"),
    # make a bid
    path('make_bid', views.make_bid, name="item-make_bid"),

]