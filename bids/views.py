from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# my bids
def my_bids(request):
    return render(request, 'bids/my_bids.html')

# make_bid
def make_bid(request):
    return render(request, 'bids/make_bid.html')

# ckeckout
def checkout_phase1(request):
    return render(request, 'bids/checkout_phase1.html')

def checkout_phase2(request):
    return render(request, 'bids/checkout_phase2.html')

def checkout_phase3(request):
    return render(request, 'bids/checkout_phase3.html')
