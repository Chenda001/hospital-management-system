from django.db import models


# Home Page (Index)
class HomeContent(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True)
    welcome_message = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

# About Page
class AboutSection(models.Model):
    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.heading

# Services Page
class Service(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)  # Optional: For frontend icons
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

# Contact Page
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.email}"

class Footer(models.Model):
    company_name = models.CharField(default='Pwani Hospital', max_length=100)
    copyright_text = models.CharField( default='Welcome to Pwani Hospital', max_length=200)
    facebook_link = models.URLField( default='https://www.facebook.com/share/1ZajeB2twA/', blank=True, null=True)
    twitter_link = models.URLField( default='https://x.com/Pwani001Hos', blank=True, null=True)
    linkedin_link = models.URLField( default='https://www.linkedin.com/in/pwani-hospital-851703376/', blank=True, null=True)
    email = models.EmailField( default='pwanihospital001@gmail.com', blank=True, null=True)
    phone = models.CharField(default='+254 700 000 000', max_length=20, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Footer - {self.company_name}"
