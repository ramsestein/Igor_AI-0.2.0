#-------------------------------------------------------------------------
#-------------------------------------------------------------------------

#Importamos todo lo necesario
import sys
import io
import os
import json
#import pyttsx
import time
from chatterbot import ChatBot
from chatterbot.training.trainers import ChatterBotCorpusTrainer
import traceback
import __future__
from Bio import Entrez

from src import abrir_ente
from src import copia_ente
from src import crea_ente
from src import borrado_ente
from src import trato_texto

from med import pudmed

import ordenes

def ConAPIAI(nombre,ai,languaje,bot):
	while True:
	#Si dio error, reutiliza el valor de antes
	#Esto es peligroso, porque a efectos practicos, si no es un error con la API, podria dar un bucle infinito, CUIDADO POSIBLE BUG
		valor = raw_input("User-> ")
		print ('.............................................')
		#Envia valor a api.ai
		request = ai.text_request()
		request.lang = languaje
		request.query = valor
		#Separamos las ordenes por subcadenas
		lista_ordenes = valor.split()
		#Hecemos un selector de las funciones
		count = ordenes.Ordenes(lista_ordenes,nombre,"terminal")
		if count == 0:
			web_html = request.getresponse()
			response = web_html.read()
			#Convertimos json a array para usarlo
			resultado = json.loads(response)
			cadena_resultado_final = resultado['result']['fulfillment']['speech']
			if cadena_resultado_final == '':
				print nombre			
				cadena_resultado_final = bot.get_response(valor)
				print ('.............................................')
			else:
				print nombre			
				print cadena_resultado_final
				print ('.............................................')


def SinAPIAI(nombre,bot):
	while True:
		#Si dio error, reutiliza el valor de antes
		#Esto es peligroso, porque a efectos practicos, si no es un error con la API, podria dar un bucle infinito, CUIDADO POSIBLE BUG
		valor = raw_input("User-> ")
		print ('.............................................')
		#Separamos las ordenes por subcadenas
		lista_ordenes = valor.split()
		#Hecemos un selector de las funciones
		count = ordenes.Ordenes(lista_ordenes,nombre,"terminal")
		if count == 0:
			print nombre			
			cadena_resultado_final = bot.get_response(valor)
			print ('.............................................')