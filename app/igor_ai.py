#!/usr/bin/python2.7

#Importamos todas las librerias e iniciamos sistemas:
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
import httplib
import urllib

from src import abrir_ente
from src import copia_ente
from src import crea_ente
from src import borrado_ente
from src import trato_texto

from med import pudmed

import voz
import terminal

try:
    import apiai
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir))
    import apiai

def igor_ai():

	print ('.............................................')

	#Sacamos los datos de stats y api
	stat_datos = trato_texto.leertxtv1("stats.txt")
	api_datos = trato_texto.leertxtv2("api.txt")

	print ("Se inicia en modo " + stat_datos[5]) 
	print ('.............................................')


	control = 0

	#Datos API.AI e iniciamos
	CLIENT_ACCESS_TOKEN = api_datos[0]
	SUBSCRIPTION_KEY = api_datos [1]
	if api_datos[0] == "" or api_datos[1] == "":
		print "No se conocen datos de API.AI. Utilice 'python setup.py api'"
		print ('.............................................')
		control = control + 1
	else:
		ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIPTION_KEY)

	#Datos Bing e iniciamos
	clientId = api_datos[2]
	clientSecret = api_datos[3]
	if api_datos[2] == "" or api_datos[3] == "":
		print "No se conocen datos de Bing Speech. Utilice 'python setup.py api'"
		control = control + 2
	else:
		ttsHost = "https://speech.platform.bing.com"
		params = urllib.urlencode({'grant_type': 'client_credentials', 'client_id': clientId, 'client_secret': clientSecret, 'scope': ttsHost})
		headers = {"Content-type": "application/x-www-form-urlencoded"}
		AccessTokenHost = "oxford-speech.cloudapp.net"
		path = "/token/issueToken"

	#Iniciamos ChatterBot
	bot = ChatBot(stat_datos[0], storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter", logic_adapters=["chatterbot.adapters.logic.ClosestMatchAdapter"], input_adapter="chatterbot.adapters.input.TerminalAdapter", output_adapter="chatterbot.adapters.output.TerminalAdapter",	database="chatterbot-database")

	#Entrenamiento de ChatterBot
	bot.set_trainer(ChatterBotCorpusTrainer)
	try:
		bot.train(stat_datos[3])	
	except:
		print "**Error al entrenar con corpus - Modo Sin Entrenamiento ON**"
		print ('.............................................')
		pass

	#Damos nuestros datos de PudMed, iniciando servicio
	Entrez.email = stat_datos[2]

	if stat_datos[1] == "es_ES":
		languaje = "es"
	elif stat_datos[1] == "us_US":
		language = "us"
	else:
		languaje = "es"

	nombre = stat_datos[0] + ": "
	voice = " -" + stat_datos[4]


	if control == 0:
		if stat_datos[5] == "terminal" or stat_datos[5] == "terminal\n":
			print ('.............................................')
			terminal.ConAPIAI(nombre,ai,languaje,bot)
		elif stat_datos[5] == "voz" or stat_datos[5] == "voz\n":
			print ('.............................................')
			voz.VozConAPIAI(stat_datos[1],voice,ttsHost,params,headers,AccessTokenHost,path,ai,languaje,nombre,bot)
		else:
			print "Error al cargar modo voz o servidor, se inicia en modo de depuracion"
			print ('.............................................')
			terminal.ConAPIAI(nombre,ai,languaje,bot)

	elif control == 1:
		if stat_datos[5] == "terminal" or stat_datos[5] == "terminal\n":
			print ('.............................................')
			terminal.SinAPIAI(nombre,bot)
		elif stat_datos[5] == "voz" or stat_datos[5] == "voz\n":
			print ('.............................................')
			voz.VozSinAPIAI(stat_datos[1],voice,ttsHost,params,headers,AccessTokenHost,path,languaje,nombre,bot)
		else:
			print "Error al cargar modo voz o servidor, se inicia en modo de depuracion"
			print ('.............................................')
			terminal.SinAPIAI(nombre,bot)
	
	elif control == 2:
		if stat_datos[5] == "terminal" or stat_datos[5] == "terminal\n":
			print ('.............................................')
			terminal.ConAPIAI(nombre,ai,languaje,bot)
		elif stat_datos[5] == "voz" or stat_datos[5] == "voz\n":
			print ('.............................................')
			print "No se puede iniciar el modo voz. Error Bing Speech"
			print ('.............................................')
			terminal.ConAPIAI(nombre,ai,languaje,bot)
		else:
			print "Error al cargar modo voz o servidor, se inicia en modo de depuracion"
			print ('.............................................')
			terminal.ConAPIAI(nombre,ai,languaje,bot)

	elif control == 3:
		if stat_datos[5] == "terminal" or stat_datos[5] == "terminal\n":
			print ('.............................................')
			terminal.SinAPIAI(nombre,bot)
		elif stat_datos[5] == "voz" or stat_datos[5] == "voz\n":
			print ('.............................................')
			print "No se puede iniciar el modo voz. Error Bing Speech"
			print ('.............................................')
			terminal.SinAPIAI(nombre,bot)
		else:
			print "Error al cargar modo voz o servidor, se inicia en modo de depuracion"
			print ('.............................................')
			terminal.SinAPIAI(nombre,bot)

def igor_aiServ(valor):
	#Sacamos los datos de stats y api
	stat_datos = trato_texto.leertxtv1("stats.txt")
	api_datos = trato_texto.leertxtv2("api.txt")

	control = 0

	#Datos API.AI e iniciamos
	CLIENT_ACCESS_TOKEN = api_datos[0]
	SUBSCRIPTION_KEY = api_datos [1]
	if api_datos[0] == "" or api_datos[1] == "":
		control = 1
	else:
		ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN, SUBSCRIPTION_KEY)

	#Iniciamos ChatterBot
	bot = ChatBot(stat_datos[0], storage_adapter="chatterbot.adapters.storage.MongoDatabaseAdapter", logic_adapters=["chatterbot.adapters.logic.ClosestMatchAdapter"], input_adapter="chatterbot.adapters.input.TerminalAdapter", output_adapter="chatterbot.adapters.output.TerminalAdapter",	database="chatterbot-database")

	#Entrenamiento de ChatterBot
	bot.set_trainer(ChatterBotCorpusTrainer)
	try:
		bot.train(stat_datos[3])	
	except:
		pass

	#Damos nuestros datos de PudMed, iniciando servicio
	Entrez.email = stat_datos[2]

	if stat_datos[1] == "es_ES":
		languaje = "es"
	elif stat_datos[1] == "us_US":
		language = "us"
	else:
		languaje = "es"

	nombre = stat_datos[0] + ": "
	voice = " -" + stat_datos[4]


	if control == 0:
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
				cadena_resultado_final = bot.get_response(valor)
		else:
			cadena_resultado_final = "Se realizó la acción correctamente"
	else:
		lista_ordenes = valor.split()
		#Hecemos un selector de las funciones
		count = ordenes.Ordenes(lista_ordenes,nombre,"terminal")
		if count == 0:
			cadena_resultado_final = bot.get_response(valor)
		else:
			cadena_resultado_final = "Se realizó la acción correctamente"

	array_to_return = [cadena_resultado_final,stat_datos[0],stat_datos[1]]

	return array_to_return

igor_ai()