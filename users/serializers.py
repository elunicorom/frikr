# -*- coding: utf-8 -*-
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.Serializer):

	id=serializers.ReadOnlyField() # solo lectura
	first_name=serializers.CharField()
	last_name=serializers.CharField()
	username=serializers.CharField()
	email=serializers.EmailField()
	password=serializers.CharField()

	def create(self,validated_data):
		#crea una instancia de User a partir de los datos de validated_data 
		#que contiene valores deserializados
		#validated_data: diccionario con los datos del usuario

		instance=User()
		return self.update(instance,validated_data)

		

	def update(self,instance,validated_data):
		instance.firts_name=validated_data.get('first_name')
		instance.last_name=validated_data.get('last_name')
		instance.username=validated_data.get('username')
		instance.email=validated_data.get('email')
		instance.set_password(validated_data.get('password'))
		instance.save()

		return instance