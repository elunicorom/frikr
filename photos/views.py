from django.http import HttpResponse
from django.shortcuts import render
from photos.models import Photo,PUBLIC


# vistas son controladores :v --- Manejan Url
def home(request):
	photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
	context = {
		'photos_list': photos
	}
	return render(request,'photos/home.html',context)

def detail(request,pk):
	"""
	carga la pagina de detalle de una foto
	:param request: Httpresponse
	:param pk: id de la foto
	:return  Httpresponse
	"""
	"""
	try:
		photo = Photo.objects.get(pk=pk)
	except Photo.DoesNotExist:
		photo=None
	except Photo.MultipleObjects:
		photo=None
	"""
	possible_photos = Photos.objects.filter(pk=pk)
	photo
