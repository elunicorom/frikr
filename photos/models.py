# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models


COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
	(COPYRIGHT,'Copyright'),
	(COPYLEFT,'Copylef'),
	(CREATIVE_COMMONS,'Creative Commons')
)

PUBLIC='PUB'
PRIVATE='PRI'

VISIBILITY = (
	(PUBLIC,'Publica'),
	(PRIVATE,'Privada')
)

class Photo(models.Model):
	owner = models.ForeignKey(User)
	name = models.CharField(max_length=150)
	url = models.URLField()
	#blank=TRue hace que el campo sea opcional
	descripcion = models.TextField(blank=True,default="")
	#automaticamente coge el momento actual
	created_at = models.DateTimeField(auto_now_add=True)
	#auto_now=True actualiza automatico
	modified_at = models.DateTimeField(auto_now=True)
	license = models.CharField(max_length=3,choices=LICENSES)
	visibility = models.CharField(max_length=3,choices=VISIBILITY,default=PUBLIC)
	def _unicode_(self):
		return self.name