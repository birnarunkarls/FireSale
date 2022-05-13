from django.shortcuts import render, redirect
from item.models import Item, Bid
from checkout.forms.checkout_form import CheckoutForm, RatingForm
from django.contrib.auth.models import User
from checkout.models import Checkout

# Create your views here.


# ckeckout

#def checkout_phase1(request, id):
#    item = Item.objects.filter(pk=id).first()
#    return render(request, 'checkout/checkout_phase1.html', {
#        'item': item,
#        'name': item.name,
#        'id': id
#    })


def checkout_phase1(request, id):
    item = Item.objects.filter(pk=id).first()
    user = User.objects.filter(pk=item.seller.id).first()
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            checkout = form.save(commit=False)
            checkout.item = item
            checkout.user = user
            checkout.save()
            return redirect('checkout-rating', user.id)
    return render(request, 'checkout/checkout_rating.html', {
        'form': CheckoutForm(),
        'item': item,
        'name': item.name,
        'id': id
    })


def rating(request, id):
    item = Item.objects.filter(pk=id).first()
    user = User.objects.filter(pk=id).first()
    print(user)
    if request.method == 'POST':
        form = RatingForm(data=request.POST)
        if form.is_valid():
            rating = form.save(commit=False)
            rating.seller = user
            rating.save()
            return redirect('checkout-checkout_phase2', user.id)
    return render(request, 'checkout/checkout_rating.html', {
        'form': RatingForm()
    })


def checkout_phase2(request,id):
    item = Item.objects.filter(seller__id=id).first()
    bid = Bid.objects.filter(item__id=item.id).all()
    checkout = Checkout.objects.filter(item__id=item.id)
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
    print(checkout_info)

    return render(request, 'checkout/checkout_phase2.html', {
        'item': item,
        'id': id,
        'highest_bid_amount': highest_bid_amount,
        'checkout_info': checkout_info
    })

def checkout_phase3(request):
    return render(request, 'checkout/checkout_phase3.html')





