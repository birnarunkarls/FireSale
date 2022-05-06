from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from item.models import Item

# Create your views here.

# item
def item(request):
    return render(request, 'item/item.html')

# create_item
def create_item(request):
    return render(request, 'item/create_item.html')

# my checkout
def my_bids(request):
    return render(request, 'item/my_bids.html')

# make_bid
def make_bid(request):
    return render(request, 'item/make_bid.html')

def get_item_by_id(request, id):
    return render(request, 'item/item.html', {
        'item': get_object_or_404(Item, pk=id)
    })