# -*- coding: utf-8 -*-
#!/usr/bin/python2.7
from sys import path
import os
from app import igor_ai 

def inicio():
	array = []
	inicio = ""
	inicio_app = os.getcwd()
	array.extend(inicio_app.split("/"))
	for i in range(len(array) - 1):
		if i == 0:
			pass
		else:
			inicio = inicio + "/" + array[i]
	return inicio

path.append(inicio())

def application(environ, start_response):

	datos = igor_ai.igor_aiServ("hola")
    
    peticion = environ['REQUEST_URI'] 
    output = datos[0]
    # Inicio una respuesta al navegador 
    start_response('200 OK', [('Content-Type', 'text/html; charset=utf-8')]) 
    # Retorno el contenido HTML 
    return output


path.append(inicio)