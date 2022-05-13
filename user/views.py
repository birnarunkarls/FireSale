from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render, redirect

from checkout.models import Rating
from user.forms.profile_form import ProfileForm
from user.models import Profile


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

    ratings = Rating.objects.filter(seller__id=request.user.id).all()
    all_ratings = []
    for i in ratings:
        all_ratings.append(i.rating)
    if len(all_ratings) != 0:
        average_rating = round(sum(all_ratings)/len(all_ratings), 1)
    else:
        average_rating = ""

    return render(request, 'user/profile.html', {
        'form': ProfileForm(instance=profile),
        'average_rating': average_rating
    })






