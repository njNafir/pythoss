from django.contrib import admin
from django.urls import re_path

from pss.views import home_page, work_slider

urlpatterns = [
    re_path(r'^$', home_page, name='home_page'),
    re_path(r'^ws$', work_slider, name='work_slider'),
]