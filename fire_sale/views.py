from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from item.models import Item, ItemCategory


# home_page
def home_page(request):
    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        filtered_items = Item.objects.filter(name__icontains=search_filter)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'data': [{
            'id': x.id,
            'name': x.name,
            'description': x.description,
            'condition': x.condition,
            'firstImage': x.images_set.first().image
        } for x in filtered_items]})
        return render(request, 'fire_sale/home_page.html', {
            'items': filtered_items
        })

    if 'sort_by' in request.GET:
        order_by = request.GET['sort_by']
        order_by_items = Item.objects.order_by(order_by)
    #    order_by = request.GET['sort_by']
    #    print(order_by)
    #    return render(request, 'item/sort_by.html', {
    #        'items': Item.objects.order_by(order_by)
    #    })

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'data': [{
                'id': x.id,
                'name': x.name,
                'description': x.description,
                'condition': x.condition,
                'firstImage': x.images_set.first().image
            } for x in order_by_items]})
        return render(request, 'fire_sale/home_page.html', {
            'items': order_by_items
        })

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