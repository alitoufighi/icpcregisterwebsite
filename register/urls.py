from django.contrib import admin
from django.urls import path, include
from register import views
from django.views.generic import TemplateView


urlpatterns = [
    path('register', views.accept),
    path('contact', TemplateView.as_view(template_name='contactUs.html')),
    path('about', TemplateView.as_view(template_name='texts.html')),
    path('', TemplateView.as_view(template_name='home.html')),
]

