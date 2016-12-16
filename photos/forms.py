# -*- coding: utf-8 -*-
from django import forms
from photos.models import Photo
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

class PhotoForm(forms.ModelForm):

	#Formulario para el modelo Photo
	class Meta:
		model = Photo
		exclude = ['owner']

	def clean(self):
		"""
		Valida si en la descripcion se han puesto tacos  en settings.BARDOWRS
		return: diccionario con los atributos si OK	
		"""

		cleaned_data=super(PhotoForm,self).clean()
		descripcion=cleaned_data.get('descripcion','')
		for badwords in BADWORDS:
			if badwords.lower() in descripcion.lower():
				raise ValidationError('La palabra {0} no esta permitida '.format(badwords))

#si todo esta ok devuelvo los datos limpios/normalizados
		return cleaned_data

