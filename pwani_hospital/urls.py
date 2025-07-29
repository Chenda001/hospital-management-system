from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),

    # Authentication URLs
    # The 'logout' URL now uses Django's built-in LogoutView.
    path('register/', views.register, name='register'), 
    path ('login/', auth_views.LoginView.as_view(template_name='pwani_hospital/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
  
]   
