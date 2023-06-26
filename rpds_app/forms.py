from django import forms
from .models import Contact, Article
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

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'author', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 700px;'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'style': 'width: 700px;'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'style': 'width: 700px;'}),
        }