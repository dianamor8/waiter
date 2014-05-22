# -*- coding: utf-8 -*-
#Saber si una cadena tiene el valor minimo requerido
def tamanio_min(cadena,minvalue):	
	if len(cadena)>= minvalue:
		return True
	return False

#Saber si una cadena tiene el valor máximo requerido
def tamanio_max(cadena,maxvalue):
	if len(cadena)<= maxvalue:
		return True
	return False



			
		