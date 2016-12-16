from django.http import HttpResponseNotFound
from django.shortcuts import render
from photos.models import Photo,PUBLIC
from photos.forms import PhotoForm
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required


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


@login_required()
def photo_create(request):
	"""
	Muestra un formulario para crear una foto y la crea si la peticion es POST
	"""

	success_message=''
	if request.method=='GET':
		form = PhotoForm()
	else:
		photo_with_owner=Photo()
		photo_with_owner.owner=request.user # 	asigno como propietario de la foto , al usuario autenicado
		form = PhotoForm(request.POST, instance=photo_with_owner)
		if form.is_valid():
			new_photo=form.save() #guarda el objeto y devuelmelo
			form=PhotoForm()
			success_message='Guardado exitoso!!'
			success_message+='<a href="{0}">'.format(reverse('photos_detail',args=[new_photo.pk]))
			success_message+= 'Ver Foto'
			success_message+= '</a>'
	
	context={
		'form': form,
		'success_message': success_message
	}

	return render(request,'photos/new_photo.html',context)