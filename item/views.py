from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import user
from item.forms.item_form import ItemCreateForm, ItemUpdateForm
from item.forms.new_bid_form import NewBidForm
from item.models import Item, Images, ItemCategory, Bid
from django.contrib.auth.models import User
from checkout.models import Rating


# Create your views here.

# item
def item(request):
    return render(request, 'item/item.html')



# my bids
@login_required
def my_bids(request, id):
    item = Item.objects.filter(pk=id).first()
    #seller = User.objects.filter(pk=id).first()
    listings = Item.objects.filter(seller__id=id)
    bids = Bid.objects.filter(buyer__id=id)
    listing_bids = Bid.objects.filter(item__id=id).all()
    #bid_items = Item.objects.filter(seller__id=seller.id)
    #bid = Bid.objects.filter(item__id=item.id).all()
    highest_bid = []
    all_listings = []
    all_bids_id = []
    all_bid_items = []

    for l in listing_bids:
        print(l)
        print(l.amount)
        highest_bid.append(l.amount)

    if len(highest_bid) != 0:
        highest_bid_offer = max(highest_bid)
    else:
        highest_bid_offer = ""

    for i in listings:
        all_listings.append(i)

    for j in bids:
        all_bids_id.append(j)

    for bid_bid in all_bids_id:
        item = Item.objects.filter(pk=bid_bid.item.id).first()
        all_bid_items.append(item)

    return render(request, 'item/my_bids.html', {
        'item': item,
        'id': id,
        'listings': listings,
        'highest_bid': highest_bid_offer,
        'bid_items': all_bid_items
    })

# my listings
#@login_required
#def my_listings(request, id):
#    item = Item.objects.filter(pk=id).first()
#
#    return render(request, 'item/my_listings.html', {
#        'item': item,
#        'id': id
#    })


# make_bid
@login_required
def make_bid(request, id):
    bid_item = Item.objects.filter(pk=id).first()
    seller = User.objects.filter(pk=bid_item.seller.id).first()
    bid = Bid.objects.filter(item__id=id).all()
    if request.method == 'POST':
        form = NewBidForm(data=request.POST)
        if form.is_valid():
            new_bid = form.save(commit=False)
            new_bid.buyer = request.user
            new_bid.item = bid_item
            new_bid.save()
            return redirect('item-my_bids', request.user.id)
    highest_bid = []
    for i in bid:
        highest_bid.append(i.amount)
    if len(highest_bid) != 0:
        highest_bid_amount = '$' + str(max(highest_bid))
    else:
        highest_bid_amount = 'No bids made'
    return render(request, 'item/make_bid.html', {
        'form': NewBidForm(),
        'bid_item': bid_item,
        'id': id,
        'seller': seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name,
        'bio': seller.profile.bio,
        'highest_bid': highest_bid_amount
    })



def get_item_by_id(request, id):
    item = Item.objects.filter(pk=id).first()
    seller = User.objects.filter(pk=item.seller.id).first()
    category = item.category
    bid = Bid.objects.filter(item__id=item.id).all()
    ratings = Rating.objects.filter(seller__id=seller.id).all()
    all_ratings = []
    highest_bid = []
    for i in bid:
        highest_bid.append(i.amount)
    if len(highest_bid) != 0:
        highest_bid_amount = '$' + str(max(highest_bid))
    else:
        highest_bid_amount = 'No bids made'
    list_of_items = []
    for i in Item.objects.filter(category__id=category.id).all():
        if i.id != id:
            list_of_items.append(i)

    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating_seller = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating_seller = ""
    return render(request, 'item/item.html', {
        'item': item,
        'seller': seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name,
        'category': category,
        'similar_items': list_of_items,
        'highest_bid': highest_bid_amount,
        'average_rating_seller': average_rating_seller
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
    #seller = User.objects.filter(pk=item.id).first()
    if request.method == "POST":
        form = ItemUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            #print(id)
            #print(seller)
            return redirect('item-my_bids', id=id)
    else:
        form = ItemUpdateForm(instance=instance)
    return render(request, 'item/update_item.html', {
        'form': form,
        'id': id
    })



def categories(request, id):
    context = ItemCategory.objects.filter(pk=id).first()
    #item = Item.objects.filter(category=context.id)
    #category = ItemCategory.objects.filter(pk=context.id)
    list_of_items = []
    for i in Item.objects.filter(category__id=id).all():
        list_of_items.append(i)
    return render(request, 'item/categories.html', {
        'id': id,
        'context': context,
        'items': list_of_items
    })


