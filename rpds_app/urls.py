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
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('connect-metamask/', views.connect_metamask, name='connect_metamask'),
    path('logout/', views.logout_view, name='logout'),
    path('submit/', views.article_create, name='submit'),
]
admin.site.site_header = 'RPDS Admin'
admin.site.index_title = 'RPDS'
