from django.db import models
from django.contrib import admin


class BanIp(models.Model):
	class Meta:
		db_table = "BanIp"

	ip_address = models.GenericIPAddressField('IP-адрес')
	status = models.BooleanField('Статус блокировки', default=True)
	time_unblock = models.DateTimeField('Время разблокировки', blank=True)
	count_page = models.IntegerField('Число запросов страниц', default=0)
	count_logo = models.IntegerField('Число запросов  логотипа', default=0)

	def __str__(self):
		return self.ip_address


class BanIpAdmin(admin.ModelAdmin):
	list_display = ('ip_address', 'status','count_page', 'count_logo', 'time_unblock')
	search_fields = ('ip_address',)