from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from item.models import Item, ItemCategory


# home_page
def home_page(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        items = [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'condition': x.condition,
            'firstImage': x.images_set.first().image
        } for x in Item.objects.filter(name__icontains=search_filter)]
        return JsonResponse({'data': items})
    context = {'items': Item.objects.all().order_by('name'), 'categories': ItemCategory.objects.all()}
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