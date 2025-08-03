from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
    path('doctors/', views.doctors, name='doctors'),
    path('doctors/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),

    # Authentication URLs
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='pwani_hospital/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
