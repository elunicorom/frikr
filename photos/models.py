from __future__ import unicode_literals

from django.db import models


COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

LICENSES = (
	(COPYRIGHT,'Copyright'),
	(COPYLEFT,'Copylef'),
	(CREATIVE_COMMONS,'Creative Commons')
)

class Photo(models.Model):

	name = models.CharField(max_length=150)
	url = models.URLField()
	#blank=TRue hace que el campo sea opcional
	descripcion = models.TextField(blank=True,default="")
	#automaticamente coge el momento actual
	created_at = models.DateTimeField(auto_now_add=True)
	#auto_now=True actualiza automatico
	modified_at = models.DateTimeField(auto_now=True)
	license = models.CharField(max_length=3,choices=LICENSES)