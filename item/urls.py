
from django.urls import path

from . import views

urlpatterns = [
    # item
    path('', views.item, name="item-item"),
    # create_item
    path('create_item/<int:id>', views.create_item, name="item-create_item"),
    # my bids
    path('my_bids/<int:id>', views.my_bids, name="item-my_bids"),
    # my listings
    path('my_listings/<int:id>', views.my_listings, name="item-my_listings"),
    # make a bid
    path('make_bid/<int:id>', views.make_bid, name="item-make_bid"),

    path('<int:id>', views.get_item_by_id, name="item-get_item_by_id"),

    path('delete_item/<int:id>', views.delete_item, name="item-delete_item"),

    path('update_item/<int:id>', views.update_item, name="item-update_item"),

    path('categories/<int:id>', views.categories, name="item-categories")

]