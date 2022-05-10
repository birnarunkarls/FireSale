
from django.urls import path

from . import views

urlpatterns = [
    # item
    path('', views.item, name="item-item"),
    # create_item
    path('create_item', views.create_item, name="item-create_item"),
    # my bids
    path('my_bids', views.my_bids, name="item-my_bids"),
    # my listings
    path('my_listings', views.my_listings, name="item-my_listings"),
    # make a bid
    path('make_bid/<int:id>', views.make_bid, name="item-make_bid"),
    #path('make_bid/<int:id>/', views.make_bid, name="item-make_bid"),

    path('<int:id>', views.get_item_by_id, name="item-get_item_by_id"),

    path('delete_item/<int:id>', views.delete_item, name="item-delete_item")

]