from django.shortcuts import render
from .models import Info, HomeSliderImage
from contact.models import SocialContact
from service.models import Service

def home_page(request):
	home_   		= True
	info 			= Info.objects.first()
	social_contact 	= SocialContact.objects.all()
	service 		= Service.objects.all()[:2]
	slider_img = HomeSliderImage.objects.filter(info_id=info.pk)
	context = {
		'home_page': home_,
		'info': info,
		'so_li': social_contact,
		'slider_img': slider_img,
		'service': service
	}
	return render(request, 'pages/home.html', context)

def work_slider(request):
	return render(request, 'slider.html', {})