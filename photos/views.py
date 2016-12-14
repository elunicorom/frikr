from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo


# vistas son controladores :v --- Manejan Url
def home(request):
	photos = Photo.objects.all().order_by('-created_at')
	context = {
		'photos_list': photos
	}
	return render(request,'photos/home.html',context)
