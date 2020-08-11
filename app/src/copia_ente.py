#Importamos todo lo necesario
import sys
import io
import os
import time

#Bloque de copiado de archivos
#Igor no tiene criterios de admin, la idea es que solo copie de home para adelante, aunque no tiene capado directamente el resto

def CopiaEnte(lista,tipo,nombre,tipo_inicio):
	envio = 0
	cadena = ''
	for i in lista:
		#print 'Esto es i: ' + i
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
				print ("Copiando archivo " + result)
				if tipo_inicio == "voz":
					os.system("./lib/mimic/bin/mimic -t " + "'Copiando archivo " + result + "'" + voice)
				else:
					pass
				os.system('cp ' + result + ' ' + direcc)
				print ('.............................................')
				break
			except:
				print nombre
				print ('No se ha podido copiar')
				if tipo_inicio == "voz":
					os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido copiar'" + voice)
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
				print ("Copiando archivo " + result)
				if tipo_inicio == "voz":
					os.system("./lib/mimic/bin/mimic -t " + "'Copiando archivo " + result + "'" + voice)
				else:
					pass
				os.system('cp ' + result + ' ' + direcc)
				print ('.............................................')
				break
			except:
				print nombre
				print ('No se ha podido copiar')
				if tipo_inicio == "voz":
						os.system("./lib/mimic/bin/mimic -t " + "'No se ha podido copiar'" + voice)
				else:
					pass
				print ('.............................................')
				break

