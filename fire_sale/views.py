from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from item.models import Item, ItemCategory, Bid


# home_page
def home_page(request):
    #item = Item.objects.filter(pk=id).first()
    #bid = Bid.objects.filter(item__id=item.id).all()

    #highest_bid = []
    #for i in bid:
    #    highest_bid.append(i.amount)

    if 'search_filter' in request.GET:
        search_filter = request.GET['search_filter']
        filtered_items = Item.objects.filter(name__icontains=search_filter)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'data': [{
                'id': x.id,
                'name': x.name,
                'description': x.description,
                'condition': x.condition,
                'firstImage': x.images_set.first().image,
                #'highest_bid': max(highest_bid)
        } for x in filtered_items]})
        return render(request, 'fire_sale/home_page.html', {
            'items': filtered_items,
            #'highest_bid': max(highest_bid)
        })

    if 'sort_by' in request.GET:
        order_by = request.GET['sort_by']
        order_by_items = Item.objects.order_by(order_by)

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'data': [{
                'id': x.id,
                'name': x.name,
                'description': x.description,
                'condition': x.condition,
                'firstImage': x.images_set.first().image,
                #'highest_bid': max(highest_bid)
            } for x in order_by_items]})
        return render(request, 'fire_sale/home_page.html', {
            'items': order_by_items,
            #'highest_bid': max(highest_bid)
        })

    return render(request, 'fire_sale/home_page.html', {
        #'highest_bid': max(highest_bid),
        'items': Item.objects.all().order_by('name'),
        'categories': ItemCategory.objects.all()
    })



# category
def category(request):
    context = {'items': Item.objects.all().order_by(request)}
    return render(request, 'fire_sale/category.html', context)

# about
def about(request):
    return render(request, 'fire_sale/about.html')


#def index(request):
#    return HttpResponse('HttpResponse: Hello World')