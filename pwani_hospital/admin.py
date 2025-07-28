from django.contrib import admin
from .models import HomeContent, AboutSection, Service, ContactMessage, Base, Footer

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    """
    Customizes the display of the Service model in the admin panel.
    """
    list_display = ('name', 'price', 'icon')
    search_fields = ('name', 'description')
    list_filter = ('price',)

# Register your other models to make them accessible in the admin panel
admin.site.register(HomeContent)
admin.site.register(AboutSection)
admin.site.register(ContactMessage)
admin.site.register(Base)
admin.site.register(Footer)



# Register your models here.
