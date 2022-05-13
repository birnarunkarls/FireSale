from django.shortcuts import render, redirect
from item.models import Item, Bid
from checkout.forms.checkout_form import CheckoutForm, RatingForm
from django.contrib.auth.models import User
from checkout.models import Checkout, Rating


def checkout_phase1(request, id):
    item = Item.objects.filter(pk=id).first()
    user = User.objects.filter(pk=item.seller.id).first()
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.item = item
            checkout.user = user
            checkout.save()
            return redirect('checkout-rating', item.id, )
    bid_status = Bid.objects.all()
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'checkout/checkout_phase1.html', {
        'form': CheckoutForm(),
        'item': item,
        'name': item.name,
        'id': id,
        'average_rating': average_rating,
        'notification': notification
    })


def rating(request, id):
    item = Item.objects.filter(pk=id).first()
    print(id)
    user = User.objects.filter(pk=id).first()
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings) / len(all_ratings), 1)
    else:
        average_rating = ""

    if request.method == 'POST':
        form = RatingForm(data=request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.seller = user
            rating.save()
            return redirect('checkout-checkout_phase2', item.id)
    bid_status = Bid.objects.all()
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'checkout/checkout_rating.html', {
        'form': RatingForm(),
        'average_rating': average_rating,
        'notification': notification
    })


def checkout_phase2(request, id):
    item = Item.objects.filter(pk=id).first()
    bid = Bid.objects.filter(item__id=id).all()
    checkout = Checkout.objects.filter(item__id=id)
    highest_bid = []
    for i in bid:
        highest_bid.append(i.amount)
    if len(highest_bid) != 0:
        highest_bid_amount = '$' + str(max(highest_bid))
    else:
        highest_bid_amount = 'No bids made'
    checkout_info = []
    for k in checkout:
        checkout_info.append(k)
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""
    bid_status = Bid.objects.all()
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    return render(request, 'checkout/checkout_phase2.html', {
        'item': item,
        'id': id,
        'highest_bid_amount': highest_bid_amount,
        'checkout_info': checkout_info,
        'average_rating': average_rating,
        'notification': notification
    })




