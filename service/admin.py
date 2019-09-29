from django.contrib import admin
from .models import ProvidedSkill, Service

class AdminProvidedSkill(admin.ModelAdmin):
	list_display 		= ['title', 'timestamp', 'updated']
	list_filter 		= ['timestamp', 'updated']
	search_field 		= ['title', 'subtitle', 'description']
	ordering 			= ['-updated', '-timestamp']

admin.site.register(ProvidedSkill, AdminProvidedSkill)


class AdminService(admin.ModelAdmin):
	list_display 		= ['title', 'timestamp', 'updated']
	list_filter 		= ['timestamp', 'updated']
	search_field 		= ['title', 'subtitle', 'description']
	ordering 			= ['-updated', '-timestamp']

admin.site.register(Service, AdminService)