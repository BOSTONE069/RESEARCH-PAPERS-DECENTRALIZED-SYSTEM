from django.contrib import admin
from .models import Contact, Article


# Register your models here.

# The code `@admin.register(Contact)` is a decorator that registers the `Contact` model with the
# Django admin site. It tells Django that the `Contact` model should be displayed and editable in the
# admin interface.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_at')


# The code `@admin.register(Article)` is a decorator that registers the `Article` model with the
# Django admin site. It tells Django that the `Article` model should be displayed and editable in the
# admin interface.

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'content', 'created_at')
