# -*- coding: utf-8 -*-

from views import PhotoQueryset
from photos.models import Photo
from photos.serializers import PhotoSerializer,PhotoListSerializer
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class PhotoListAPI(PhotoQueryset,ListCreateAPIView):

	queryset = Photo.objects.all()
	permissions_classes=(IsAuthenticatedOrReadOnly,)
	#solo decirle la clase, no instanciarla

	def get_serializer_class(self):
		return PhotoSerializer if self.request.method=="POST" else PhotoListSerializer

	def get_queryset(self):
		return self.get_photos_queryset(self.request)

class PhotoDetailAPI(PhotoQueryset,RetrieveUpdateDestroyAPIView):
	queryset = Photo.objects.all()
	serializer_class=PhotoSerializer
	permissions_classes=(IsAuthenticatedOrReadOnly,)

	def get_queryset(self):
		return self.get_photos_queryset(self.request)

