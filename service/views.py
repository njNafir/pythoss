from django.shortcuts import render
from .models import Service
from pss.models import Info
from contact.models import SocialContact

def service_page(request):
	social_link = SocialContact.objects.all()
	info_ = Info.objects.first()
	services = Service.objects.all()

	context = {
		'info': info_,
		'so_li': social_link,
		'service': services
	}

	return render(request, 'pages/services.html', context)