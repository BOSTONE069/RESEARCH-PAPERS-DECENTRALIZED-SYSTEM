from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime


# Create your models here.# The Contact class represents a contact with a name, email, and creation
# timestamp.

class Contact(models.Model):
    name = models.TextField(max_length=255)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.email} {self.name} {self.created_at}"


# The above class defines a model for an article with fields for title, author, content, and creation
# date.
class Article(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
