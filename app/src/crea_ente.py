#Importamos todo lo necesario
import sys
import io
import os
import time

#Bloque de creacion de carpetas y archivos
#Igor no tiene criterios de admin, la idea es que solo cree de home para adelante, aunque no tiene capado directamente el resto
def CreaEnte(lista,tipo,nombre,tipo_inicio):
	envio = 0
	cadena = ''
	for i in lista:
		#print 'Esto es i: ' + i
		if i.find('/') > -1:
			#Reconvertimos a cadena
			for i in lista:
				cadena = cadena +' '+ i
			if tipo == 0:
				result = cadena[6:]
				try:
					print nombre
					print ("Creando carpeta " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Creando carpeta " + result + "'" + voice)
					else:
						pass
					os.system('mkdir -p ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido crear la carpeta')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido crear la carpeta'" + voice)
					else:
						pass
					print ('.............................................')
					break
			else:
				punto_inicio = cadena.find(' crear ')
				punto_inicio = punto_inicio + 5
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Creando carpeta " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Creando carpeta " + result + "'" + voice)
					else:
						pass
					os.system('mkdir -p ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido crear la carpeta')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido crear la carpeta'" + voice)
					else:
						pass
					print ('.............................................')
					break
		else:
			#Reconvertimos a cadena
			for i in lista:
				cadena = cadena +' '+ i
			#print 'Esto es cadena: ' + cadena
			if tipo == 0:
				result = cadena[6:]
				value = data.find(' en ')
				value = value + 4
				direcc = data[value:]
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Creando archivo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Creando archivo " + result + "'" + voice)
					else:
						pass
					os.system('touch ' + result + ' ' + direcc)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido crear el archivo')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido crear el archivo'" + voice)
					else:
						pass
					print ('.............................................')
					break
			else:
				punto_inicio = cadena.find(' crear ')
				punto_inicio = punto_inicio + 5
				#Ver el directorio
				value = data.find(' en ')
				value = value + 4
				direcc = data[value:]
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Creando archivo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Creando archivo " + result + "'" + voice)
					else:
						pass
					os.system('touch ' + result + ' ' + direcc)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido crear el archivo')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido crear el archivo'" + voice)
					else:
						pass
					print ('.............................................')
					break

