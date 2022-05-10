from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from item.models import Item, Bid
from django.contrib.auth.models import User
from user.models import Profile

# Create your views here.

# item
def item(request, id):
    context = {'items': Item.objects.filter(pk=id).first()}
    return render(request, 'item/item.html', context)


# create_item
def create_item(request):
    return render(request, 'item/create_item.html')


# my checkout
def my_bids(request):
    return render(request, 'item/my_bids.html')


# make_bid
def make_bid(request, id):
    context = {'items': Item.objects.filter(pk=id).first()}
    return render(request, 'item/make_bid.html', context)


def get_item_by_id(request, id):
    item = Item.objects.filter(pk=id).first()
    seller = User.objects.filter(pk=item.seller.id).first()

    return render(request, 'item/item.html', {
        'item': item,
        "seller": seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name
    })

#def create_item(request)