from django.contrib import admin
from django.urls import path, include
from register import views
from django.views.generic import TemplateView


urlpatterns = [
    path('icpc/register', views.accept),
    path('icpc/contact', TemplateView.as_view(template_name='contactUs.html')),
    path('icpc/about', TemplateView.as_view(template_name='texts.html')),
    path('icpc/', TemplateView.as_view(template_name='home.html')),
    path('icpc/export', views.export_users_csv, name='export_users_csv'),
]

