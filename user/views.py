from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from user.forms.profile_form import ProfileForm
from user.models import Profile

# Create your views here.


# register
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    return render(request, 'user/register.html', {
        'form': UserCreationForm()
    })

# login
#def login(request):
    #return render(request, 'user/login.html')

# profile
def profile(request):
    profile = Profile.objects.filter(user=request.user).first()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user-profile')
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile)
    })


# profile_edit
def profile_edit(request):
    return render(request, 'user/profile_edit.html')



