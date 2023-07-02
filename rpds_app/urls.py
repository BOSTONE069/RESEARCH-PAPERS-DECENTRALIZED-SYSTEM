from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

# The `urlpatterns` variable is a list of URL patterns that Django will use to match incoming requests
# to the corresponding view functions. Each URL pattern is defined using the `path()` function, which
# takes three arguments: the URL pattern, the view function to be called when the pattern is matched,
# and an optional name for the URL pattern.
urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.about, name='about'),
    path('rpds/', views.rpds_app, name='rpds'),
    path('contact/', views.contact, name='contact'),
    path('success', views.success, name='success'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('connect-metamask/', views.connect_metamask, name='connect_metamask'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.article_create, name='submit'),
]
admin.site.site_header = 'RPDS Admin'
admin.site.index_title = 'RPDS'
