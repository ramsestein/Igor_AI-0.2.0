# Importar librerias de sistema
#----------------------------------------------------
#----------------------------------------------------

import sys
import io
import os
import stat

def install():
	#Instalacion automatica de las librerias
	#----------------------------------------------------
	#----------------------------------------------------

	inicio = os.getcwd()
	nub0 = raw_input ("Si tuviera alguna instalacion previa de Igor_AI se borrara. Desea continuar? [S/N]")
	print "-------------------------------------------------"
	if nub0 == "S" or nub0 == "s":
		pass
	else:
		sys.exit(0)
	print "-------------------------------------------------"
	print "Bienvenido a la instalacion de Igor_AI"
	print "-------------------------------------------------"
	print "-------------------------------------------------"
	print "Rellene los datos a continuacion sobre su Asistente Personal"
	print "-------------------------------------------------"
	nombre = raw_input("Nombre de su asistente: ")
	print "-------------------------------------------------"
	idioma = raw_input("Idioma (introduzca es_ES/us_US): ")
	print "-------------------------------------------------"
	sexo = raw_input("Sexo de su asistente (introduzca V/M): ")
	print "Si desea cambiar la voz, use 'python setup.py reinstall_voices()'"
	print "-------------------------------------------------"
	mail = raw_input("E-mail: ")
	print "-------------------------------------------------"

	dato = open ('app/stats.txt','w')
	dato.write(nombre+"-")
	dato.write(idioma+"-")
	dato.write(mail+"-")

	if idioma == "es_ES":
		dato.write("chatterbot.corpus.espanol-")
	elif idioma == "us_US":
		dato.write("chatterbot.corpus.english-")
	else:
		dato.write("chatterbot.corpus.espanol-")

	if sexo == "V" or sexo == "v":
		dato.write("cmu_us_aew.flitevox-")
	elif sexo == "M" or sexo == "M":
		dato.write("cmu_us_slt.flitevox-")
	else:
		dato.write("cmu_us_aew.flitevox-")

	dato.close()

	nub = raw_input ("Se instalaran algunas librerias para Igor_AI. Desea continuar? [S/N]")
	print "-------------------------------------------------"
	print "-------------------------------------------------"
	print "-------------------------------------------------"
	if nub == "S" or nub == "s":
		pass
	else:
		sys.exit(0)

	print "Iniciando la instalacion..."
	print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/numpy-master/")

	try:
		os.system("sudo python setup.py install")
		print "Numpy: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria numpy"
		print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/scipy-master/")
	try:
		os.system("sudo python setup.py install")
		print "Scipy: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria scipy"
		print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/api-ai-python-master/")
	try:
		os.system("sudo python setup.py install")
		print "ApiAI: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria api-ai"
		print "-------------------------------------------------"
	
	try:
		os.system("sudo apt-get install sox")
		print "SOX: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria sox"
		print "-------------------------------------------------"

	try:
		os.system("sudo apt-get install wave")
		print "WAVE: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria wave"
		print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/python-Levenshtein-0.12.0/")
	try:
		os.system("sudo python setup.py install")
		print "Levenshtein: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria levenshtein"
		print "-------------------------------------------------"

	try:
		os.system("sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927")
		os.system('echo "deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list')
		os.system("sudo apt-get update")
		os.system("sudo apt-get install -y mongodb-org")
		print "MongoDB: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria mongodb"
		print "-------------------------------------------------"
	
	try:
		os.system("sudo apt-get install apache2 libapache2-mod-wsgi")
		print "Apache2: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria Apache2+WSGI"
		print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/requests-2.10.0/")
	try:
		os.system("sudo python setup.py install")
		print "Requests: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria requests"
		print "-------------------------------------------------"
	

	os.chdir(inicio + "/app/lib/future-0.15.2/")
	try:
		os.system("sudo python setup.py install")
		print "Future: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria future"
		print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/pymongo-3.2.2/")
	try:
		os.system("sudo python setup.py install")
		print "Pymongo: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria pymongo"
		print "-------------------------------------------------"


	os.chdir(inicio + "/app/lib/ChatterBot-master/")
	try:
		os.system("sudo python setup.py install")
		print "ChatterBot: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria chatterbot"
		print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/PyAudio-0.2.9/")
	try:
		os.system("sudo apt-get install libjack-jackd2-dev portaudio19-dev")
		os.system("sudo python setup.py install")
		print "Pyaudio: OK"
		print "-------------------------------------------------"
	except:
		print "Error al instalar la libreria pyaudio"
		print "-------------------------------------------------"
	
	os.chdir(inicio + "/app/lib/biopython-1.66/")
	try:
		os.system("sudo python setup.py install")
		print "Bio: OK"
		print "-------------------------------------------------"
	except:	
		print "Error al instalar la libreria Bio"
		print "-------------------------------------------------"

	os.chdir(inicio + "/app/lib/mimic/")
	try:
		os.system("sudo apt-get install gcc")
		os.system("sudo apt-get install libasound2-dev")
		os.system("./configure")
		os.system("sudo make")
		print "Mimic: OK"
		print "-------------------------------------------------"
	except:	
		print "Error al instalar la libreria Mimic"
		print "-------------------------------------------------"
	os.chdir(inicio)


def reinstall_corpus():

	#Moviendo los corpus personalizados
	#-----------------------------------------------------
	#-----------------------------------------------------
	print "-------------------------------------------------"
	try:		
		os.system("sudo rm -R /usr/local/lib/python2.7/dist-packages/ChatterBot-0.4.1-py2.7.egg/chatterbot/corpus/data")
	except:
		pass
	try:
		os.chmod("/usr/local/lib/python2.7/dist-packages/ChatterBot-0.4.1-py2.7.egg/chatterbot/corpus",0777)
		os.system("sudo cp -r app/lib/data /usr/local/lib/python2.7/dist-packages/ChatterBot-0.4.1-py2.7.egg/chatterbot/corpus")
		os.system("sudo rm -R app/lib/ChatterBot-master/chatterbot/corpus/data")
		os.system("sudo cp -r app/lib/data lib/ChatterBot-master/chatterbot/corpus")
		os.chmod("igor_ai.py",0777)
		os.chmod("/usr/local/lib/python2.7/dist-packages/ChatterBot-0.4.1-py2.7.egg/chatterbot/corpus/data",0777)
		print "Finish"
		print "-------------------------------------------------"
	except:	
		print "Error al copiar los corpus"
		print "-------------------------------------------------"

def help():
	print "Argumentos utilizables con setup.py para con Igor_AI: "
	print "install (-i): Instala Igor_AI"
	print "reinstall_corpus (-ric): Resinstala el corpus linguistico localizado en la carpeta data, no modifica los datos incluidos en stats.txt. Deben cambiarse a mano"
	print "reinstall_voices (-riv): Cambia la voz del asistente, localizadas en la carpeta lib/mimic/voices. Para mas dudas consultar README.txt"
	print "mode (-m) + [OPTION](terminal/voz/servidor): Cambia el modo por defecto en el que inicia el asistente. Vease mas en README.txt"
	print "api (-a): Cambia las credenciales de las API que utiliza el asistente. La API de Api.AI no es de obligatorio cambio, la de Bing si. Se requieren cuenta en ambos servicios para tener un asistente totalmente personal. Ambos servicios son gratuitos y no requieren configuraciones"
	print "help (-h): Muestra esta ayuda de la instalacion"

