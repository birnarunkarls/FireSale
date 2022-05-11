from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import user
from item.forms.item_form import ItemCreateForm, ItemUpdateForm
from item.models import Item, Images, ItemCategory
from django.contrib.auth.models import User


# Create your views here.

# item
def item(request):
    return render(request, 'item/item.html')



# my bids
@login_required
def my_bids(request, id):
    item = Item.objects.filter(pk=id).first()
    return render(request, 'item/my_bids.html', {
        'item': item,
        'id': id
    })

# my listings
@login_required
def my_listings(request, id):
    item = Item.objects.filter(pk=id).first()

    return render(request, 'item/my_listings.html', {
        'item': item,
        'id': id
    })


# make_bid
@login_required
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

@login_required
def create_item(request, id):
    seller = User.objects.filter(pk=id).first()
    if request.method == "POST":
        form = ItemCreateForm(data=request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.seller = request.user
            item.save()
            item_image = Images(image=request.POST['image'], item=item)
            item_image.save()
            return redirect('fire_sale-home_page')
    else:
        form = ItemCreateForm()
        # TODO: Instance new ItemCreateForm()
    return render(request, 'item/create_item.html', {
        'form': form,
        'user.id': seller
    })

@login_required
def delete_item(request,id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('fire_sale-home_page')

@login_required
def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    if request.method == "POST":
        form = ItemUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('item-my_listings', id=id)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'item/update_item.html', {
        'form': form,
        'id': id
    })



def categories(request, id):
    context = Item.objects.filter(category=id).all()
    #category = ItemCategory.objects.filter(pk=context.id)
    print(context)
    #print(category)
    return render(request, 'item/categories.html', {
        'id': id,
        #'category': category
    })


