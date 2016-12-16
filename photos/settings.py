# -*- coding: utf-8 -*-

from django.conf import settings # importa el settings del proyecto

COPYRIGHT = 'RIG'
COPYLEFT = 'LEF'
CREATIVE_COMMONS = 'CC'

DEFAULT_LICENSES = (
	(COPYRIGHT,'Copyright'),
	(COPYLEFT,'Copylef'),
	(CREATIVE_COMMONS,'Creative Commons')
)

LICENSES=getattr(settings,'LICENSES',DEFAULT_LICENSES)