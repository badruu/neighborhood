from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
import datetime as dt
from .models import Hoods, Business
from users.models import Profile
from .forms import *
from django.contrib.auth.decorators import login_required

@login_required(login_url="/users/login/")
def index(request):
    users = Profile.objects.all()
    current_user=request.user
    hoods = Hoods.objects.all()
    businesses = Business.objects.all()
    return render(request, 'hoods/index.html', {"current_user":current_user, "businesses":businesses, "hoods":hoods, "users":users})

@login_required(login_url="/users/login/")
def createneighbourhood(request):
    '''
    View function for new service page
    '''
    current_user=request.user
    admin=Profile.objects.get(user=current_user)
    user = Profile.objects.get(user=current_user)
    hoods = user.neighbourhood_id
    
    if request.method == 'POST':
        form = NeighbourhoodForm(request.POST, request.FILES)
        if form.is_valid():
            hoods = form.save(commit=False)
            hoods.admin = current_user
            hoods.population = 1
            hoods.timestamp = timezone.now()
            hoods.save()
        return redirect('welcome')
    else:
        form = NeighbourhoodForm()

    return render(request, 'hoods/hoodform.html', {"form":form, "current_user":current_user, "admin":admin, "user":user, "hoods":hoods})

@login_required(login_url="/users/login/")
def createbusiness(request):
    '''
    View function for new service page
    '''
    current_user=request.user
    admin=Profile.objects.get(user=current_user)
    user = Profile.objects.get(user=current_user)
    biznas = user.business_id
    hoods = user.neighbourhood_id
    
    if request.method == 'POST':
        form = BusinessForm(request.POST, request.FILES)
        if form.is_valid():
            biznas = form.save(commit=False)
            biznas.user = current_user
            biznas.hood_id = hoods
            biznas.timestamp = timezone.now()
            biznas.save()
        return redirect('welcome')
    else:
        form = BusinessForm()

    return render(request, 'hoods/businessform.html', {"form":form, "current_user":current_user, "admin":admin, "user":user, "biznas":biznas})