from django.contrib import admin
from .models import Info, HomeSliderImage

class AdminHomeSliderImage(admin.TabularInline):
	model = HomeSliderImage
	extra = 1

class AdminInfo(admin.ModelAdmin):
	list_display = ['__str__']
	list_filter = ['timestamp']

	inlines = [AdminHomeSliderImage]

admin.site.register(Info, AdminInfo)