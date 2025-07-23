from django.shortcuts import render

def return_base(request):
    return render(request, 'pwani_hospital/base.html')

def index(request):
   return render(request, 'pwani_hospital/index.html')

def about(request):
    return render(request, 'pwani_hospital/about.html')

def services(request):
    return render(request, 'pwani_hospital/services.html')

def contact(request):
    return render(request, 'pwani_hospital/contact.html')
def Footer(request):
    footer = Footer.objects.first()
    return render(request, 'pwani_hospital/base.html', {'footer': footer})
