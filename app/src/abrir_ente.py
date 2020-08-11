#Importamos todo lo necesario
import sys
import io
import os
import time

#Bloque de apertura de archivos y programas
#Igor no tiene criterios de admin, la idea es que solo borre de home para adelante, aunque no tiene capado directamente el resto

def AbrirEnte(lista,tipo,nombre,tipo_inicio):
	cadena = ''
	for i in lista:
		#print 'Esto es i: ' + i
		if i.find('.') > -1:
			#Reconvertimos a cadena
			for i in lista:
				cadena = cadena +' '+ i
			#print 'Esto es cadena: ' + cadena
			if tipo == 0:
				result = cadena[6:]
				try:
					print nombre
					print ("Abriendo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Abriendo " + result + "'" + voice)
					else:
						pass
					result = result + ' &'
					os.system('run-mailcap ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido abrir')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido abrir'" + voice)
					else:
						pass
					print ('.............................................')
					break
			else:
				punto_inicio = cadena.find(' abre ')
				punto_inicio = punto_inicio + 5
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Abriendo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Abriendo " + result + "'" + voice)
					else:
						pass
					result = result + ' &'
					os.system('run-mailcap ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido abrir')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido abrir'" + voice)
					else:
						pass
					print ('.............................................')
					break
		elif i.find('/') > -1:
			#Reconvertimos a cadena
			for i in lista:
				cadena = cadena +' '+ i
			#print 'Esto es cadena: ' + cadena
			if tipo == 0:
				result = cadena[6:]
				try:
					print nombre
					print ("Abriendo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Abriendo " + result + "'" + voice)
					else:
						pass
					result = result + ' &'
					os.system('nautilus ' + result)
					print ('.............................................')					
					break
				except:
					print nombre
					print ('No se ha podido abrir')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido abrir'" + voice)
					else:
						pass
					print ('.............................................')
					break
			else:
				punto_inicio = cadena.find(' abre ')
				punto_inicio = punto_inicio + 5
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Abriendo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Abriendo " + result + "'" + voice)
					else:
						pass
					result = result + ' &'
					os.system('nautilus ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido abrir')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido abrir'" + voice)
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
				try:
					print nombre
					print ("Abriendo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Abriendo " + result + "'" + voice)
					else:
						pass
					print ('.............................................')
					result = result + ' &'
					os.system(result)
					break
				except:
					print nombre
					print ('No se ha podido abrir')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido abrir'" + voice)
					else:
						pass
					print ('.............................................')
					break
			else:
				punto_inicio = cadena.find(' abre ')
				punto_inicio = punto_inicio + 5
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Abriendo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Abriendo " + result + "'" + voice)
					else:
						pass
					result = result + ' &'
					os.system(result)
					break
				except:
					print nombre
					print ('No se ha podido abrir')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido abrir'" + voice)
					else:
						pass
					print ('.............................................')
					break

