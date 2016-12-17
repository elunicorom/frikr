# -*- coding: utf-8 -*-
from django.views.generic import View  #Vista generica de django
from django.contrib.auth.models import User
from django.http import HttpResponse
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response

class UserListAPI(APIView):

	def get(self,request):
		users=User.objects.all()
		serializer=UserSerializer(users,many=True)
		serializer_users=serializer.data #lista de diccionarios
		return Response(serializer_users)
