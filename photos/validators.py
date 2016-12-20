# -*- coding: utf-8 -*-
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

def badwords_detector(value):
		"""
		Valida si en 'value' se han puesto tacos en settings.BARDOWRS
		return: diccionario con los atributos si OK	
		"""
		for badwords in BADWORDS:
			if badwords.lower() in descripcion.lower():
				raise ValidationError('La palabra {0} no esta permitida '.format(badwords))

#si todo esta ok devuelvo los datos limpios/normalizados
		return True
