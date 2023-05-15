from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Home, name='home'),
    path('about/', views.about, name='about'),
    path('rpds/', views.rpds_app, name='rpds'),
    path('contact/', views.contact, name='contact'),
    path('success', views.success, name='success'),
    path('connect-metamask/', views.connect_metamask, name='connect_metamask'),
]
admin.site.site_header = 'RPDS Admin'
admin.site.index_title = 'RPDS'
