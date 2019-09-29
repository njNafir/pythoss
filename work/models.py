from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from django.db.models.signals import pre_save
from service.models import ProvidedSkill
from django.urls import reverse
import random, string

def get_unique_path(how_many=12):
	range_ = how_many
	chars = string.ascii_lowercase + string.digits
	path = ''.join(random.choice(chars) for _ in range(range_))
	return path

PROJECT_TYPE = (
		('Web Design', 'Web Design'),
		('Web Development', 'Web Development'),
		('Full Stack', 'Full Stack'),
	)

def store_project_thumb_image_path(instance, filename):
	slug 	= instance.slug
	path 	= "project_thumb/{slug}/{filename}".format(slug=slug, filename=filename)
	return path

class Store(models.Model):
	title 			= models.CharField(max_length=255)
	slug 			= models.CharField(max_length=255)
	subtitle 		= models.CharField(max_length=255, blank=True, null=True)
	thumbnail 		= models.ImageField(upload_to=store_project_thumb_image_path)
	description 	= models.TextField()
	web_link 		= models.CharField(max_length=255, blank=True, null=True)
	provided_skill 	= models.ManyToManyField(ProvidedSkill)
	project_type 	= models.CharField(max_length=120, choices=PROJECT_TYPE, default='Full Stack')
	timestamp 		= models.DateTimeField(auto_now_add=True)
	updated 		= models.DateTimeField(auto_now=True)

	class Meta:
		ordering 	= ['-updated', '-timestamp']

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('work_single', args=[self.slug])

def get_unique_store_path(how_many=17):
	slug = get_unique_path(how_many)
	while Store.objects.filter(slug=slug).exists():
		slug = get_unique_path(how_many)
	return slug

def store_pre_save_reciever(sender, instance, *args, **kwargs):
	if not instance.slug:
		slug = get_unique_store_path()
		instance.slug = slug

pre_save.connect(store_pre_save_reciever, sender=Store)

def store_project_gallery_image_path(instance, filename):
	slug 	= get_unique_path(17)
	path 	= "projects/{slug}/{filename}".format(slug=slug, filename=filename)
	return path

class StoreProjectGalleryImage(models.Model):
	title 					= models.CharField(max_length=120, blank=True, null=True)
	project_gallery_image 	= models.ForeignKey(Store, on_delete=models.PROTECT)
	files 					= models.FileField(upload_to=store_project_gallery_image_path)


	def get_absolute_url(self):
		return reverse('project_gallery_image', args=[self.files])

def store_project_file_path(instance, filename):
	slug 	= get_unique_path(17)
	path 	= "projects/{slug}/{filename}".format(slug=slug, filename=filename)
	return path

class StoreProjectFile(models.Model):
	title 					= models.CharField(max_length=120, blank=True, null=True)
	project_file 			= models.ForeignKey(Store, on_delete=models.PROTECT)
	files 					= models.FileField(upload_to=store_project_file_path, storage=FileSystemStorage(location=settings.PROT_ROOT))
	free 					= models.BooleanField(default=False)
	user_required 			= models.BooleanField(default=True)
