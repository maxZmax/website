from django.contrib import admin
from .models import BanIp, BanIpAdmin


admin.site.register(BanIp,BanIpAdmin)