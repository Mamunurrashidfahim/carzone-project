from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Teams
from cars.models import Car

def home(request):
    teams =Teams.objects.all()
    featured_car =Car.objects.order_by('-create_at').filter(is_featured=True)
    all_cars =Car.objects.order_by('-create_at')
    return render(request,'pages/home.html',context={'teams':teams,'featured_car':featured_car,'all_cars':all_cars})

def about(request):
    teams =Teams.objects.all()
    return render(request,'pages/about.html',context={'teams':teams})

def services(request):
    return render(request,'pages/services.html',context={})

def contact(request):
    return render(request,'pages/contact.html',context={})