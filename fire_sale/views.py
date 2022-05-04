from django.http import HttpResponse
from django.shortcuts import render


# home_page
def home_page(request):
    return render(request, 'fire_sale/home_page.html')

# category
def category(request):
    return render(request, 'fire_sale/category.html')

# about
def about(request):
    return render(request, 'fire_sale/about.html')


#def index(request):
#    return HttpResponse('HttpResponse: Hello World')