from django.shortcuts import render
from django.http import HttpResponse
from pages.models import Teams


def home(request):
    teams =Teams.objects.all()
    return render(request,'pages/home.html',context={'teams':teams})

def about(request):
    teams =Teams.objects.all()
    return render(request,'pages/about.html',context={'teams':teams})

def services(request):
    return render(request,'pages/services.html',context={})

def contact(request):
    return render(request,'pages/contact.html',context={})