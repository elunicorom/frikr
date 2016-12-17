# -*- coding: utf-8 -*-
from django.views.generic import View  #Vista generica de django
from django.contrib.auth.models import User
from django.http import HttpResponse
from users.serializers import UserSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class UserListAPI(APIView):

	def get(self,request):
		users=User.objects.all()
		serializer=UserSerializer(users,many=True)
		serializer_users=serializer.data #lista de diccionarios
		return Response(serializer_users)


class UserDetailAPI(APIView):

	def get(self,request,pk):
		user = get_object_or_404(User,pk=pk)
		serializer=UserSerializer(user)
		return Response(serializer.data)