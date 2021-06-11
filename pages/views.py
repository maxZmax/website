from django.shortcuts import render
from django.views import View
from django.utils import timezone
from django.http import HttpResponse
from ipware import get_client_ip
from .models import *


def checker(html, request, *self):
		ip = get_client_ip(request)[0]

		obj, created = BanIp.objects.get_or_create(
			defaults={'ip_address': ip, 'time_unblock': timezone.now()}, 
			ip_address=ip)

		if obj.status is False and (obj.count_page - obj.count_logo) > 0:
			obj.status = True
			obj.time_unblock = timezone.now() + timezone.timedelta(minutes=5)
			obj.save()

		if obj.status is True and obj.time_unblock > timezone.now():

			return 'block.html'
			
		elif obj.status is True and obj.time_unblock < timezone.now():
			obj.status = False
			obj.count_logo = 0
			obj.count_page = 0
			obj.save()

		if obj.status is False:
			obj.count_page += 1
			obj.save()

			return html



def page(request):
	page = checker('main.html', request)

	return render(request, page)


def ads(request, adid):
	html = f'p_ad{adid}.html'
	page = checker(html, request)

	return render(request, page)

def logo(request):
	ip = get_client_ip(request)[0]
	obj = BanIp.objects.get(ip_address=ip)
	obj.count_logo += 1
	obj.save()

	return HttpResponse('/static/img/logo.png')