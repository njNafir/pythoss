from django.db import models

def bg_image_upload_path(instance, filename):
	path = "bg_img/{f}".format(f=filename)
	return path

class Info(models.Model):
	site_title 						= models.CharField(max_length=120)

	language_question 				= models.CharField(max_length=120)
	language_title 					= models.CharField(max_length=120)
	language_description 			= models.TextField()
	language_final_text 			= models.CharField(max_length=120)
	language_background_image 		= models.ImageField(upload_to=bg_image_upload_path)

	framework_question 				= models.CharField(max_length=120)
	framework_title 				= models.CharField(max_length=120)
	framework_description 			= models.TextField()
	framework_final_text 			= models.CharField(max_length=120)
	framework_background_image 		= models.ImageField(upload_to=bg_image_upload_path)

	timestamp 						= models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = [
			'-timestamp'
		]

	def __str__(self):
		return self.site_title


def home_slider_image_upload_path(instance, filename):
	path = "home_slider_img/{f}".format(f=filename)
	return path

class HomeSliderImage(models.Model):
	title 							= models.CharField(max_length=120, blank=True, null=True)
	caption 						= models.CharField(max_length=250, blank=True, null=True)
	image 							= models.ImageField(upload_to=home_slider_image_upload_path)
	info 							= models.ForeignKey(Info, on_delete=models.CASCADE)
	timestamp 						= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title