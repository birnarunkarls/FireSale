from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# item
def item(request):
    return render(request, 'item/item.html')

# create_item
def create_item(request):
    return render(request, 'item/create_item.html')



