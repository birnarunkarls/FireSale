from django.http import HttpResponse
from django.shortcuts import render

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

