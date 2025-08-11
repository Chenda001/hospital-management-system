from django.db import models
from django.utils import timezone

class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    welcome_message = models.TextField(blank=True)

    def __str__(self):
        return self.title

class AboutSection(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)
    image = models.ImageField(upload_to='about_images/', null=True, blank=True)

    def __str__(self):
        return self.heading

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Add this field to store the icon's CSS classes
    icon = models.CharField(
        max_length=50, 
        blank=True, 
        help_text="Enter a Font Awesome class, e.g., 'fas fa-heartbeat'. Find icons at fontawesome.com."
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    # Add this field to store the icon's CSS classes
    icon = models.CharField(
        max_length=50, 
        blank=True, 
        help_text="Enter a Font Awesome class, e.g., 'fas fa-heartbeat'. Find icons at fontawesome.com."
    )

    def __str__(self):
        return self.name

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialty = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='doctors/', help_text="Upload a profile picture for the doctor.")

    def __str__(self):
        return f"Dr. {self.name} - {self.specialty}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"

class Base(models.Model):
    """
    Model for basic, site-wide settings like the site name.
    """
    site_name = models.CharField(max_length=100, default="Pwani Hospital")

    def __str__(self):
        return self.site_name

    class Meta:
        verbose_name_plural = "Base Settings"
        

class Footer(models.Model):
    """
    Model to store all the information needed for the site's footer.
    """
    company_name = models.CharField(max_length=100)
    copyright_text = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=20, blank=True)
    facebook_link = models.URLField(default='#', blank=True)
    twitter_link = models.URLField(default='#', blank=True)
    linkedin_link = models.URLField(default='#', blank=True)

    def __str__(self):
        return f"Footer Settings for {self.company_name}"
        return f"Footer Settings for {self.company_name}"