from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Contact(models.Model):
    email = models.EmailField()


