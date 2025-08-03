from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import ContactMessage

class UserRegisterForm(UserCreationForm):
    """
    A form for creating new users. Includes email field.
    """
    email = forms.EmailField()

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('email',)

class ContactForm(forms.ModelForm):
    """
    A form for handling contact messages, based on the ContactMessage model.
    """
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email Address'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Message Subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your Message', 'rows': 5}),
        }

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        """
        model = User
        fields = UserCreationForm.Meta.fields + ['email']
        """