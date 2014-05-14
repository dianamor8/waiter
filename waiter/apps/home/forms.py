# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
	Email = forms.EmailField(widget=forms.EmailInput(), label='Email')
	Titulo = forms.CharField(widget=forms.TextInput())
	Texto = forms.CharField(widget=forms.Textarea())	
    # TODO: Define form fields here

class LoginForm(forms.Form):
    # TODO: Define form fields here
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Usuario','required': True,}), label='Usuario')
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Contraseña','required': True,}), label='Contraseña')

    
    