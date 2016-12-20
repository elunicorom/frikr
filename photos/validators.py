# -*- coding: utf-8 -*-
from photos.settings import BADWORDS
from django.core.exceptions import ValidationError

def badwords_detector(value):
		"""
		Valida si en 'value' se han puesto tacos en settings.BARDOWRS
		return: diccionario con los atributos si OK	
		"""
		for badword in BADWORDS:
			if badword.lower() in value.lower():
				raise ValidationError(u'La palabra {0} no esta permitida '.format(badword))

#si todo esta ok devuelvo los datos limpios/normalizados
		return True
