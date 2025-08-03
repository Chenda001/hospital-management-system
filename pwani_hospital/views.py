from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login
from .models import HomeContent, AboutSection, Service, Doctor
from .forms import UserRegisterForm, ContactForm

def index(request):
    # Fetch the first (and likely only) HomeContent object from the database
    home_content = HomeContent.objects.first()
    featured_doctors = Doctor.objects.all()[:3] # Fetch 3 doctors
    context = {
       'home_content': home_content,
       'doctors': featured_doctors
    }
    return render(request, 'pwani_hospital/index.html', context)

def about(request):
    about_section = AboutSection.objects.first()
    context = {
        'about': about_section
    }
    return render(request, 'pwani_hospital/about.html', context)
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

def doctors(request):
    """
    Displays a list of all doctors.
    """
    doctors_list = Doctor.objects.all()
    context = {
        'doctors': doctors_list
    }
    return render(request, 'pwani_hospital/doctors.html', context)

def doctor_detail(request, doctor_id):
    """
    Displays the detailed bio of a single doctor.
    """
    doctor = get_object_or_404(Doctor, pk=doctor_id)
    context = {
        'doctor': doctor
    }
    return render(request, 'pwani_hospital/doctor_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully! We will get back to you shortly.')
            return redirect('contact')
        else:
            messages.error(request, 'There was an error with your submission. Please check the fields and try again.')
    else:
        form = ContactForm()
    return render(request, 'pwani_hospital/contact.html', {'form': form})

def register(request):
    """
    Handles user registration.
    """
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, f'Account created successfully! Welcome, {user.username}.')
            return redirect('home')
    else:
        form = UserRegisterForm()
    return render(request, 'pwani_hospital/register.html', {'form': form})
