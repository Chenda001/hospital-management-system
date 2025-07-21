from django.shortcuts import render

def index(request):
    return render(request, 'pwani_hospital/index.html')

def about(request):
    return render(request, 'pwani_hospital/about.html')

def contact(request):
    return render(request, 'pwani_hospital/contact.html')

def services(request):
    return render(request, 'pwani_hospital/services.html')
