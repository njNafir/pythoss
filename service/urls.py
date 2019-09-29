from django.contrib import admin
from django.urls import path, re_path, include
from .views import service_page

urlpatterns = [
    re_path(r'^service$', service_page, name='service_page'),
]
