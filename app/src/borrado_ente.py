#Importamos todo lo necesario
import sys
import io
import os
import time

#Bloque de borrado de archivos y carpetas
#Igor no tiene criterios de admin, la idea es que solo borre de home para adelante, aunque no tiene capado directamente el resto
def BorraEnte(lista,tipo,nombre,tipo_inicio):
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
					print ("Borrando carpeta " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Borrando carpeta " + result + "'" + voice)
					else:
						pass
					os.system('rm -R ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido borrar')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido borrar'" + voice)
					else:
						pass	
					print ('.............................................')
					break
			else:
				punto_inicio = cadena.find(' borra ')
				punto_inicio = punto_inicio + 5
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Borrando carpeta " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Borrando carpeta " + result + "'" + voice)
					else:
						pass
					os.system('rm -R ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido borrar')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido borrar'" + voice)
					else:
						pass
					print ('.............................................')
					break
		else:
			#Reconvertimos a cadena
			for i in lista:
				cadena = cadena +' '+ i
			if tipo == 0:
				result = cadena[6:]
				try:
					print nombre
					print ("Borrando archivo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Borrando archivo " + result + "'" + voice)
					else:
						pass
					os.system('rm ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido borrar')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido borrar'" + voice)
					else:
						pass
					print ('.............................................')
					break
			else:
				punto_inicio = cadena.find(' borra ')
				punto_inicio = punto_inicio + 5
				#Como el comando util estara despues de la accion, borramos la cadena anterior para mandar la orden
				result = cadena[punto_inicio:]
				try:
					print nombre
					print ("Borrando archivo " + result)
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'Borrando archivo " + result + "'" + voice)
					else:
						pass
					os.system('rm -R ' + result)
					print ('.............................................')
					break
				except:
					print nombre
					print ('No se ha podido borrar')
					if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido borrar'" + voice)
					else:
						pass
					print ('.............................................')
					break

