from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home_page(request):
    return render(request, 'fire_sale/home_page.html')


def about(request):
    return render(request, 'fire_sale/about.html', {
        'list': [
            {
                'name': 'Arnar',
                'description': 'Desc 1'
            },
            {
                'name': 'Arnar2',
                'description': 'Desc 2'
            }
        ]
    })


#def index(request):
#    return HttpResponse('HttpResponse: Hello World')