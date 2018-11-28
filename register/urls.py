from django.contrib import admin
from django.urls import path, include
from register import views
from django.views.generic import TemplateView

urlpatterns = [
    path('register', views.accept),
    path('', TemplateView.as_view(template_name='index.html')),
]
