from django.http import HttpResponse
from django.shortcuts import render



# vistas son controladores :v --- Manejan Url
def home(request):
    return HttpResponse("Hola a todos :v")
