# -*- coding: utf-8 -*-
from django import forms

class LoginForm(forms.Form):
	
	usr=forms.CharField(label="Nombre de Usuario")
	pwd=forms.CharField(label="Password", widget=forms.PasswordInput())
