from django.shortcuts import render

# Create your views here.


# ckeckout
def checkout_phase1(request):
    return render(request, 'checkout/checkout_phase1.html')

def checkout_phase2(request):
    return render(request, 'checkout/checkout_phase2.html')

def checkout_phase3(request):
    return render(request, 'checkout/checkout_phase3.html')
