from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo,PUBLIC
from photos.forms import PhotoForm


# vistas son controladores :v --- Manejan Url
def home(request):
	photos = Photo.objects.filter(visibility=PUBLIC).order_by('-created_at')
	context = {
		'photos_list': photos[:5]
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
	possible_photos = Photo.objects.filter(pk=pk)
	photo = possible_photos[0] if len(possible_photos)==1 else None
	if photo is not None:
		#cargar la plantilla de detalle
		context = {
			'photo':photo
		}
		return render(request,'photos/detail.html',context)
	else:
		return HttpresponseNotFound('No existe la foto') # 404 Not found

def photo_create(request):
	"""
	Muestra un formulario para crear una foto y la crea si la peticion es POST
	"""

	if request.method=='GET':
		form = PhotoForm
	else:
		form = PhotoForm(request.POST)
		if form.is_valid():
			new_photo=form.save()#guarda el objeto y devuelmelo
	
	context={
		'form': form
	}

	return render(request,'photos/new_photo.html',context)