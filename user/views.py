from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from user.forms.profile_form import ProfileForm
from user.models import Profile
from checkout.models import Rating
from statistics import mean
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
    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('user-profile')
    print('hello')
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    print(round(mean(all_ratings),1))
    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile),
        'average_rating': round(mean(all_ratings),1)
    })


# profile_edit
def profile_edit(request):
    return render(request, 'user/profile_edit.html')






