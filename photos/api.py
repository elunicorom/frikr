# -*- coding: utf-8 -*-


from photos.models import Photo
from photos.serializers import PhotoSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView

class PhotoListAPI(ListCreateAPIView):

	queryset = Photo.objects.all()
	serializer_class=PhotoSerializer#solo decirle la clase, no instanciarla

class PhotoDetailAPI(RetrieveUpdateDestroyAPIView):
	queryset = Photo.objects.all()
	serializer_class=PhotoSerializer


