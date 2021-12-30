from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'pages/home.html',context={})

def about(request):
    return render(request,'pages/about.html',context={})

def services(request):
    return render(request,'pages/services.html',context={})

def contact(request):
    return render(request,'pages/contact.html',context={})