from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


# register
def register(request):
    return render(request, 'user/register.html')

# login
def login(request):
    return render(request, 'user/login.html')

# profile
def profile(request):
    return render(request, 'user/profile.html')

# profile_edit
def profile_edit(request):
    return render(request, 'user/profile_edit.html')



