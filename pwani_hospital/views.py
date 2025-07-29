from django.shortcuts import render, redirect
from django.contrib import messages
from .models import HomeContent, AboutSection, Service, ContactMessage

def index(request):
    try:
        # Fetch the first (and likely only) HomeContent object from the database
        home_content = HomeContent.objects.first()
    except HomeContent.DoesNotExist:
        home_content = None  # Handle case where the table or data does not exist

    context = {
        'home_content': home_content
    }
    return render(request, 'pwani_hospital/index.html', context)

def about(request):
    about_section = AboutSection.objects.first()
    context = {
        'about': about_section
    }
    return render(request, 'pwani_hospital/about.html', context)

def services(request):
    services_list = Service.objects.all()
    context = {
        'services': services_list
    }
    return render(request, 'pwani_hospital/services.html', context)

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if name and email and subject and message:
            ContactMessage.objects.create(name=name, email=email, subject=subject, message=message)
            messages.success(request, 'Your message has been sent successfully! We will get back to you shortly.')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill out all fields.')

    return render(request, 'pwani_hospital/contact.html')
