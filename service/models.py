from django.db import models

class ProvidedSkill(models.Model):
	title 				= models.CharField(max_length=50)
	subtitle 			= models.CharField(max_length=120)
	description 		= models.TextField(blank=True, null=True)
	timestamp 			= models.DateTimeField(auto_now_add=True)
	updated 			= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = [
			'-updated',
			'-timestamp'
		]

	def __str__(self):
		return self.title

class Service(models.Model):
	title 				= models.CharField(max_length=50)
	subtitle 			= models.CharField(max_length=120)
	description 		= models.TextField()
	provided_skill		= models.ManyToManyField(ProvidedSkill)
	timestamp 			= models.DateTimeField(auto_now_add=True)
	updated 			= models.DateTimeField(auto_now=True)

	class Meta:
		ordering = [
			'-updated',
			'-timestamp'
		]
	def __str__(self):
		return self.title

	