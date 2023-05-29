from django import forms
from .models import Contact
from django.contrib.auth.forms import UserCreationForm

# This is a Django form class for a contact form that includes an email field with specific attributes
# for styling and validation.
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter email address...",
                'aria-label': "Enter email address...",
                'data-sb-validations': "required,email"
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Enter name...",
                'aria-label': "Enter name...",
                'data-sb-validations': "required,name"
            })
        }
