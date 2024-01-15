from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path

from research import settings
from . import views
from django.conf.urls.static import static

from .views import subscriber

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('subscribe/', subscriber, name='subscribe'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
    path('projects/', views.projects, name='projects'),
    path('team/', views.team, name='team'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)