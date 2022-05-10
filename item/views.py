from django.shortcuts import render, redirect, get_object_or_404

from item.forms.item_form import ItemCreateForm, ItemUpdateForm
from item.models import Item, Images
from django.contrib.auth.models import User


# Create your views here.

# item
def item(request):
    return render(request, 'item/item.html')


# create_item
def create_item(request):
    return render(request, 'item/create_item.html')


# my bids
def my_bids(request):
    return render(request, 'item/my_bids.html')

# my listings
def my_listings(request, id):
    item = Item.objects.filter(pk=id).first()

    return render(request, 'item/my_listings.html', {
        'item': item,
        'id': id
    })


# make_bid
def make_bid(request, id):
    bid_item = Item.objects.filter(pk=id).first()
    seller = User.objects.filter(pk=bid_item.seller.id).first()

    return render(request, 'item/make_bid.html', {
        'bid_item': bid_item,
        'id': id,
        'seller': seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name,
        'bio': seller.profile.bio
    })


def get_item_by_id(request, id):
    item = Item.objects.filter(pk=id).first()
    seller = User.objects.filter(pk=item.seller.id).first()

    return render(request, 'item/item.html', {
        'item': item,
        'seller': seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name
    })

def create_item(request):
    if request.method == "POST":
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save()
            item_image = Images(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('fire_sale-home_page')
    else:
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'item/create_item.html', {
        'form': form
    })

def delete_item(request,id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('fire_sale-home_page', {
        'item': item,
        'id': id
    })

def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        print(1)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'item/update_item.html', {
        'form': form,
        'id': id
    })