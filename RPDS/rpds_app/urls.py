from django.urls import path
from . import views
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.Home, name='home'),
    path('rpds/', views.rpds_app, name='rpds'),
    path("contact/", views.contact, name='contacts'),
]
admin.site.site_header = 'Research Papers Decentralized System'
admin.site.index_title = 'RPDS'
