from django.shortcuts import render

from item.forms.item_form import ItemCreateForm
from item.models import Item
from django.contrib.auth.models import User


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
    item = Item.objects.filter(pk=id).first()
    seller = User.objects.filter(pk=item.seller.id).first()

    return render(request, 'item/item.html', {
        'item': item,
        "seller": seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name
    })

def create_item(request):
    if request.method == "POST":
        print(1)
    else:
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'item/create_item.html', {
        'form': form
    })