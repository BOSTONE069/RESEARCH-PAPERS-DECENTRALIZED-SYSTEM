from django.contrib import admin
from .models import Contact, Article

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
     list_display = ('name', 'email', 'created_at')


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
     list_display = ('title', 'author', 'content', 'created_at')