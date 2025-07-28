from .models import Footer, Base, Service

def site_context(request):
    """A context processor to add site-wide settings to the context."""
    # Fetch up to 4 services to display in the footer
    footer_services = Service.objects.all()[:4]
    return {
        'footer': Footer.objects.first(),
        'base_settings': Base.objects.first(),
        'footer_services': footer_services,
    }