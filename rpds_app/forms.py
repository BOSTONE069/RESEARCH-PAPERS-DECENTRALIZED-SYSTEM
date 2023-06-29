from django import forms
from .models import Contact, Article
from django.contrib.auth.forms import UserCreationForm

# This is a Django form class for a contact form that includes an email field with specific attributes
# for styling and validation.
# The ContactForm class is a form that allows users to enter their name and email address.
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

# The `ArticleForm` class is a form that is used to create or update an `Article` model, with fields
# for `title`, `author`, and `content`, and custom styling for the form inputs.
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 700px;'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 700px;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 700px;'}),
        }