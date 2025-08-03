from django.contrib import admin
from .models import HomeContent, AboutSection, Service, Doctor, ContactMessage, Base, Footer

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Service model in the admin panel.
    """
    list_display = ('name', 'price', 'icon')
    search_fields = ('name', 'description')
    list_filter = ('price',)

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Doctor model in the admin panel.
    """
    list_display = ('name', 'specialty')
    search_fields = ('name', 'specialty')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    """
    Customizes the display for contact messages to be read-only.
    """
    list_display = ('name', 'email', 'subject', 'submitted_at')
    search_fields = ('name', 'email', 'subject', 'message')
    list_filter = ('submitted_at',)
    readonly_fields = ('name', 'email', 'subject', 'message', 'submitted_at')

# Register your other models to make them accessible in the admin panel
admin.site.register(HomeContent)
admin.site.register(AboutSection)
admin.site.register(Base)
admin.site.register(Footer)