from django.http import HttpResponse
from django.shortcuts import render
from item.models import Item


# home_page
def home_page(request):
    context = {'items': Item.objects.all().order_by('name')}
    return render(request, 'fire_sale/home_page.html', context)

# category
def category(request):
    context = {'items': Item.objects.all().order_by(request)}
    return render(request, 'fire_sale/category.html', context)

# about
def about(request):
    return render(request, 'fire_sale/about.html')


#def index(request):
#    return HttpResponse('HttpResponse: Hello World')