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

	def validate_username(self,data):
		#Valida si existe un usuario con ese nombre

		users = User.objects.filter(username=data)
#Si estoy creando(No hay instancia), comprobamos usuarios con mismo nombre
		if not self.instance and len(users)!=0:
			raise serializers.ValidationError(u"Ya existe un usuario con ese nombre")
			#si estoy actualizando, el nuevo nombre es diferene al de la instancia y existen usuarios
			#ya registrados con ese nombre
		elif self.instance and self.instance.username != data and len(users)!=0:
			raise serializers.ValidationError(u"Ya existe un usuario con ese nombre")
		else:
			return data