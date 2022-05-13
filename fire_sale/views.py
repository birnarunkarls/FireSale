from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from item.models import Item, ItemCategory, Bid
from checkout.models import Rating


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
                'firstImage': x.images_set.first().image,
        } for x in filtered_items]})
        return render(request, 'fire_sale/home_page.html', {
            'items': filtered_items
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
            } for x in order_by_items]})
        return render(request, 'fire_sale/home_page.html', {
            'items': order_by_items
        })

    bid_status = Bid.objects.all()
    notification = 'False'
    for i in bid_status:
        if i.status == "accepted":
            notification = 'True'
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""

    return render(request, 'fire_sale/home_page.html', {
        'items': Item.objects.all().order_by('name'),
        'categories': ItemCategory.objects.all(),
        'average_rating': average_rating,
        'notification': notification
    })

