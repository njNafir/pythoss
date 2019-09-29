from django.contrib import admin
from django.urls import path, re_path
from .views import work_all, work_full_stack, work_developed, work_designed, work_single

urlpatterns = [
	re_path(r'^work/$', work_all, name='work_page'),
	re_path(r'^work/dev-des$', work_full_stack, name='work_full_stack'),
	re_path(r'^work/dev$', work_developed, name='work_developed'),
	re_path(r'^work/des$', work_designed, name='work_designed'),
	re_path(r'^work/(?P<slug>[-\w]+)$', work_single, name='work_single')
]