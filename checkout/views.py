from django.shortcuts import render, redirect
from item.models import Item
# Create your views here.


# ckeckout

def checkout_phase1(request, id):
    item = Item.objects.filter(pk=id).first()
    return render(request, 'checkout/checkout_phase1.html', {
        'item': item,
        'name': item.name,
        'id': id
    })

def checkout_phase2(request,id):
    item = Item.objects.filter(pk=id).first()
    return render(request, 'checkout/checkout_phase2.html', {
        'item': item,
        'name': item.name,
        'id': id
    })

def checkout_phase3(request):
    return render(request, 'checkout/checkout_phase3.html')


def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('rating')
    return render(request, 'checkout/checkout_phase1.html', {
        'form': CheckoutForm()
    })
