from django.urls import path
from . import views


urlpatterns = [
	path('logo', views.logo),
	path('ads/<int:adid>/', views.ads),
    path('', views.page)
]