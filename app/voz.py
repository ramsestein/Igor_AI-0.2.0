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
import pyaudio
import wave
import sys

from src import abrir_ente
from src import copia_ente
from src import crea_ente
from src import borrado_ente
from src import trato_texto

from med import pudmed

import ordenes



def VozConAPIAI(idioma,voice,ttsHost,params,headers,AccessTokenHost,path,ai,languaje,nombre,bot):

	chunk = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	RECORD_SECONDS = 4
	WAVE_OUTPUT_FILENAME = "output.wav"

	if idioma == "us_US":
		idioma_real = "us-US"
	else:
		idioma_real = "es-ES"

	conn = httplib.HTTPSConnection(AccessTokenHost)
	loop = 0


	while True:
		p = pyaudio.PyAudio()
		stream = p.open(format = FORMAT, channels = CHANNELS, rate = RATE, input = True, frames_per_buffer = chunk)

		print ('.............................................')
		print "* Grabando. 4seg"
		frames = []
		for i in range(0, RATE / chunk * RECORD_SECONDS):
  	  		data = stream.read(chunk)
  	  		frames.extend(data)
		print "* Grabado"
		print ('.............................................')

		stream.close()
		p.terminate()

		# write data to WAVE file
		data = b''.join(frames)
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(data)
		wf.close()

		# Connect to server to get the Oxford Access Token
		conn.request("POST", path, params, headers)
		response = conn.getresponse()
		#print(response.status, response.reason)

		data1 = response.read()
		conn.close()
		accesstoken = data1.decode('UTF-8')
		#print ("Oxford Access Token: " + accesstoken)

		#decode the object from json
		if loop == 0:
			ddata=json.loads(accesstoken)
			access_token = ddata['access_token']

		# Read the binary from wave file
		f = open('output.wav','rb')
		try:
  		  body = f.read();
		finally:
  		  f.close()
  	
		headers = {"Content-type": "audio/wav; samplerate=8000", "Authorization": "Bearer " + access_token}

		#Connect to server to recognize the wave binary
		conn = httplib.HTTPSConnection("speech.platform.bing.com")
		conn.request("POST", "/recognize/query?scenarios=ulm&appid=D4D52672-91D7-4C74-8AD8-42B1D98141A5&locale="+idioma_real+"&device.os=wp7&version=3.0&format=json&requestid=1d4b6030-9099-11e0-91e4-0800200c9a66&instanceid=1d4b6030-9099-11e0-91e4-0800200c9a66", body, headers)
		response = conn.getresponse()
		print ('.............................................')
		print "Estado del Servicio:"
		print(response.status, response.reason)
		print "Idioma del Servicio: "
		print idioma_real
		print ('.............................................')
		value_json = response.read()
		data1 = json.loads(value_json)
		#print data1
		valor = data1["results"][0]["lexical"]
		print("User -> " + data1["results"][0]["lexical"])
		conn.close()
		print ('.............................................')
		#Envia valor a api.ai
		request = ai.text_request()
		request.lang = languaje
		request.query = valor
		#Separamos las ordenes por subcadenas
		lista_ordenes = valor.split()
		#Hecemos un selector de las funciones
		count = ordenes.Ordenes(lista_ordenes,nombre,"voz")
		loop = 1
		if count == 0:
				web_html = request.getresponse()
				response = web_html.read()
				#Convertimos json a array para usarlo
				resultado = json.loads(response)
				cadena_resultado_final = resultado['result']['fulfillment']['speech']
				if cadena_resultado_final == '':
					print nombre			
					habla = bot.get_response(valor)
					print ('.............................................')
					os.system("./lib/mimic/bin/mimic -t " + "'" + habla + "'" + voice)
					print ('.............................................')
				else:
					print nombre			
					print cadena_resultado_final
					print ('.............................................')
					os.system("./lib/mimic/bin/mimic -t " + "'" + cadena_resultado_final + "'" + voice)
					print ('.............................................')



def VozSinAPIAI(idioma,voice,ttsHost,params,headers,AccessTokenHost,path,nombre,bot):
	chunk = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 1
	RATE = 44100
	RECORD_SECONDS = 4
	WAVE_OUTPUT_FILENAME = "output.wav"

	if idioma == "us_US":
		idioma_real = "us-US"
	else:
		idioma_real = "es-ES"

	conn = httplib.HTTPSConnection(AccessTokenHost)
	loop = 0

 	while True:
		p = pyaudio.PyAudio()
		stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = chunk)
		print ('.............................................')
		print "* Grabando. 4seg"
		frames = []
		for i in range(0, RATE / chunk * RECORD_SECONDS):
  	  		data = stream.read(chunk)
    		frames.append(data)
		print "* Grabado"
		print ('.............................................')

		stream.close()
		p.terminate()

		# write data to WAVE file
		data = b''.join(frames)
		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(data)
		wf.close()

		# Connect to server to get the Oxford Access Token
		conn.request("POST", path, params, headers)
		response = conn.getresponse()
		#print(response.status, response.reason)

		data1 = response.read()
		conn.close()
		accesstoken = data1.decode('UTF-8')
		if loop == 1:
			ddata=json.loads(accesstoken)
			access_token = ddata['access_token']

		# Read the binary from wave file
		f = open('output.wav','rb')
		try:
  		  body = f.read();
		finally:
  		  f.close()

		headers = {"Content-type": "audio/wav; samplerate=8000", "Authorization": "Bearer " + access_token}
	
		#Connect to server to recognize the wave binary
		conn = httplib.HTTPSConnection("speech.platform.bing.com")
		conn.request("POST", "/recognize/query?scenarios=ulm&appid=D4D52672-91D7-4C74-8AD8-42B1D98141A5&locale="+idioma_real+"&device.os=wp7&version=3.0&format=json&requestid=1d4b6030-9099-11e0-91e4-0800200c9a66&instanceid=1d4b6030-9099-11e0-91e4-0800200c9a66", body, headers)
		response = conn.getresponse()
		print ('.............................................')
		print "Estado del Servicio:"
		print(response.status, response.reason)
		print ('.............................................')
		value_json = response.read()
		data1 = json.loads(value_json)
		valor = data["results"][0]["lexical"]
		print("User -> " + data1["results"][0]["lexical"])
		conn.close()
		print ('.............................................')
		#Separamos las ordenes por subcadenas
		lista_ordenes = valor.split()
		#Hecemos un selector de las funciones
		count = ordenes.Ordenes(lista_ordenes,nombre,"voz")
		loop = 1
		if count == 0:
			print nombre			
			habla = bot.get_response(valor)
			os.system("./lib/mimic/bin/mimic -t " + "'" + habla + "'" + voice)
			print ('.............................................')
			