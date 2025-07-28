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
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    # Note: You will still need to create URLs and views for 'login' and 'register'.
]
