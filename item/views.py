from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

import user
from item.forms.item_form import ItemCreateForm, ItemUpdateForm
from item.forms.new_bid_form import NewBidForm
from item.models import Item, Images, ItemCategory, Bid
from django.contrib.auth.models import User
from checkout.models import Rating

# my bids
@login_required
def my_bids(request, id):
    listings = Item.objects.filter(seller__id=id)
    bids = Bid.objects.filter(buyer__id=id)
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""
    highest_bid = []
    all_listings = []
    all_bids_id = []
    all_bid_items = []
    my_listed_items_with_bids = []
    every_bid = []
    for y in Bid.objects.filter(buyer__id=id).all():
        every_bid.append(y)
    new_list = []
    for b in listings:
        for a in Bid.objects.filter(item__id=b.id):
            new_list.append(a)
            my_listed_items_with_bids.append(Item.objects.filter(pk=b.id).first())

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
    bid_status = Bid.objects.filter(buyer__id=request.user.id)
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'item/my_bids.html', {
        'id': id,
        'listings': listings,
        'bid_items': all_bid_items,
        'my_listed_items_with_bids': my_listed_items_with_bids,
        'every_bid': every_bid,
        'new_list': new_list,
        'average_rating': average_rating,
        'notification': notification
    })


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
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""
    bid_status = Bid.objects.filter(buyer__id=request.user.id)
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'item/make_bid.html', {
        'form': NewBidForm(),
        'bid_item': bid_item,
        'id': id,
        'seller': seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name,
        'bio': seller.profile.bio,
        'highest_bid': highest_bid_amount,
        'average_rating': average_rating,
        'notification': notification
    })


@login_required
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

    ratings_user = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings_user = []
    for i in ratings_user:
        all_ratings_user.append(i.rating)
    if len(all_ratings_user) != 0:
        average_rating = round(sum(all_ratings_user)/len(all_ratings_user), 1)
    else:
        average_rating = ""

    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating_seller = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating_seller = ""
    bid_status = Bid.objects.filter(buyer__id=request.user.id)
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'item/item.html', {
        'item': item,
        'seller': seller,
        'full_name': seller.profile.first_name + ' ' + seller.profile.last_name,
        'category': category,
        'similar_items': list_of_items,
        'highest_bid': highest_bid_amount,
        'average_rating_seller': average_rating_seller,
        'average_rating': average_rating,
        'notification': notification
    })



@login_required
def create_item(request, id):
    seller = User.objects.filter(pk=id).first()
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""
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
    bid_status = Bid.objects.filter(buyer__id=request.user.id)
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'item/create_item.html', {
        'form': form,
        'user.id': seller,
        'average_rating': average_rating,
        'notification': notification
    })

@login_required
def delete_item(request, id):
    item = get_object_or_404(Item, pk=id)
    item.delete()
    return redirect('fire_sale-home_page')


@login_required
def delete_bid(request, id):
    bid = get_object_or_404(Bid, item__id=id)
    bid.delete()
    return redirect('fire_sale-home_page')


@login_required
def accept_bid(request, id):
    bid = get_object_or_404(Bid, item__id=id)
    bid.status = 'accepted'
    bid.save()
    return redirect('fire_sale-home_page')



@login_required
def update_item(request, id):
    instance = get_object_or_404(Item, pk=id)
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings) / len(all_ratings), 1)
    else:
        average_rating = ""
    if request.method == "POST":
        form = ItemUpdateForm(data=request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('fire_sale-home_page', id=id)
    else:
        form = ItemUpdateForm(instance=instance)
    bid_status = Bid.objects.filter(buyer__id=request.user.id)
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'item/update_item.html', {
        'form': form,
        'id': id,
        'average_rating': average_rating,
        'notification': notification
    })

@login_required
def categories(request, id):
    context = ItemCategory.objects.filter(pk=id).first()
    list_of_items = []
    for i in Item.objects.filter(category__id=id).all():
        list_of_items.append(i)
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""
    bid_status = Bid.objects.filter(buyer__id=request.user.id)
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'item/categories.html', {
        'id': id,
        'context': context,
        'items': list_of_items,
        'average_rating': average_rating,
        'notification': notification
    })


