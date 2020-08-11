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

def Ordenes(lista_ordenes,nombre,tipo):
	for i in lista_ordenes:
		#Si cumple una funcion, sigue este camino y pasa de las ai
		count = 0
		if i == 'Abre' or i == 'Open':
			abrir_ente.AbrirEnte(lista_ordenes,0,nombre,tipo)
			count = 1
			break
		if i == 'abre' or i == 'open':
			abrir_ente.AbrirEnte(lista_ordenes,1,nombre,tipo)
			count = 1
			break
		if i == 'copia' or i == 'copy':
			copia_ente.CopiaEnte(lista_ordenes,1,nombre,tipo)
			count = 1
			break
		if i == 'Copia' or i == 'Copy':
			copia_ente.CopiaEnte(lista_ordenes,0,nombre,tipo)
			count = 1
			break
		if i == 'Crea' or i == 'Create':
			crea_ente.CreaEnte(lista_ordenes,0,nombre,tipo)
			count = 1
			break
		if i == 'crea' or i == 'create':
			crea_ente.CreaEnte(lista_ordenes,1,nombre,tipo)
			count = 1
			break
		if i == 'Borra' or i == 'Delete':
			borrado_ente.BorraEnte(lista_ordenes,0,nombre,tipo)
			count = 1
			break
		if i == 'borra' or i == 'delete':
			borrado_ente.BorraEnte(lista_ordenes,1,nombre,tipo)
			count = 1
			break
		if i == 'busca' or i == 'search':
			pudmed.BuscarEn(lista_ordenes,1,nombre,tipo)
			count = 1
			break
		if i == 'Busca' or i == 'Search':
			pudmed.BuscarEn(lista_ordenes,0,nombre,tipo)
			count = 1
			break
		if i == 'Salir' or i == 'salir' or i =="Exit" or i == "exit":
			sys.exit(0)
			break
				
	return count