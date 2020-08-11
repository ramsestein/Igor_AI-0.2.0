#Importamos todo lo necesario
from Bio import Entrez
import traceback
import __future__
import sys
import io
import os
import time

#Bloque de busqueda en PudMed
#Crea un archivo con los datos de la busqueda

def BuscarEn(lista,tipo,nombre,tipo_inicio):
	envio = 0
	data = ''
	result = ''
	for i in lista:
		#print 'Esto es i: ' + i
		#Reconvertimos a cadena
		for i in lista:
			data = data +' '+ i
		#print 'Esto es cadena: ' + cadena
		if tipo == 0:
			iniciador = data[6:]
			borrador = iniciador.split()
			for m in borrador:
				if m == "en":
					break
				else:
					result = result + ' ' + m
			value = data.find(' en ')
			value = value + 4
			direcc = data[value:]
			#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
			nom_archivo = "busq/" + result + '_' + direcc + '.txt'
			print nombre
			print ("Buscando " + result + ' en ' + direcc)
			if tipo_inicio == "voz":
				os.system("./lib/mimic/bin/mimic -t " + "'Buscando " + result + ' en ' + direcc + "'" + voice)
			else:
				pass
			#Bloque Busqueda en PudMed
			search_results = Entrez.read(Entrez.esearch(db=direcc, term=result, reldate=365, datetype="pdat",	usehistory="y"))
			count = int(search_results["Count"])
			print nombre
			print("Encontrados %i resultados" % count)
			if tipo_inicio == "voz":
				os.system("./lib/mimic/bin/mimic -t " + "'Encontrados " + count + " resultados'" + voice)
			else:
				pass
			batch_size = 10
			out_handle = open(nom_archivo, "w")
			for start in range(count):
				try:
           				fetch_handle = Entrez.efetch(db=direcc,rettype="medline", retmode="text", retstart=start, retmax=batch_size, webenv=search_results["WebEnv"], query_key = search_results["QueryKey"])
        			except HTTPError as err:
            				if 500 <= err.code <= 599:
							print nombre
                			print("Error desde el servidor %s" % err)
            	if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Error desde el servidor:  " + err + "'" + voice)
    		info = fetch_handle.read()
    		fetch_handle.close()
    		out_handle.write(info)
		out_handle.close()
		print nombre
		print ("Guardada la busqueda como " + nom_archivo)
		if tipo_inicio == "voz":
			os.system("./lib/mimic/bin/mimic -t " + "'Guardada la busqueda como " + nom_archivo + "'" + voice)
		else:
			pass
		break
	else:
			punto_inicio = data.find(' busca ')
			punto_inicio = punto_inicio + 6
			#Ver el directorio
			value = data.find(' en ')
			value = value + 4
			direcc = data[value:]
			#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
			nom_archivo = "busq/" + result + '_' + direcc + '.txt'
			iniciador = data[punto_inicio:]
			borrador = iniciador.split()
			for m in borrador:
				if m == "en":
					break
				else:
					result = result + ' ' + m
			print nombre			
			print ("Buscando " + result + ' en ' + direcc)
			if tipo_inicio == "voz":
				os.system("./lib/mimic/bin/mimic -t " + "'Buscando " + result + ' en ' + direcc + "'" + voice)
			else:
				pass
			#Bloque Busqueda en PudMed
			search_results = Entrez.read(Entrez.esearch(db=direcc, term=result, reldate=365, datetype="pdat",	usehistory="y"))
			count = int(search_results["Count"])
			print nombre
			print("Encontrados %i resultados" % count)
			if tipo_inicio == "voz":
				os.system("./lib/mimic/bin/mimic -t " + "'Encontrados " + count + " resultados'" + voice)
			else:
				pass
			batch_size = 10
			out_handle = open(nom_archivo, "w")
			for start in range(count):
				try:
           				fetch_handle = Entrez.efetch(db=direcc,rettype="medline", retmode="text", retstart=start, retmax=batch_size, webenv=search_results["WebEnv"], query_key = search_results["QueryKey"])
        			except HTTPError as err:
            				if 500 <= err.code <= 599:
							print nombre
                			print("Error desde el servidor %s" % err)
    	      		if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Error desde el servidor:  " + err + "'" + voice)
    	info = fetch_handle.read()
    	fetch_handle.close()
   	out_handle.write(info)
	out_handle.close()
	print nombre
	print ("Guardada la busqueda como " + nom_archivo)
	if tipo_inicio == "voz":
		os.system("./lib/mimic/bin/mimic -t " + "'Guardada la busqueda como " + nom_archivo + "'" + voice)
	else:
		pass


