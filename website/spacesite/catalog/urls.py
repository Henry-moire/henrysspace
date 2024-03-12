from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('contact', views.contact, name='contact'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('services', views.services, name='services'),
]
