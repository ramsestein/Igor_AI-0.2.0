import sys
import io
import os
import stat

def leertxtv1(dato):
    array = []
    archi=open(dato,'r')
    linea = "init"
    while linea!="":
        linea=archi.readline()
	array.extend(linea.split("-"))
    archi.close()
    #print array
    return array

#leertxt("stats.txt")

def leertxtv2(dato):
    array = []
    archi=open(dato,'r')
    linea = "init"
    while linea!="":
        linea=archi.readline()
	array.extend(linea.split("+_+"))
    archi.close()
    #print array
    return array

def mode(modo):
	stat_datos = leertxtv1("app/stats.txt")
	dato = open ("app/stats.txt","w")
	dato.write(stat_datos[0]+"-"+stat_datos[1]+"-"+stat_datos[2]+"-"+stat_datos[3] + stat_datos[4])
	if modo == "terminal":
		dato.write("terminal")
		print ("Su asistente se iniciara en modo terminal")
		print "-------------------------------------------------"
	elif modo == "voz":
		dato.write("voz")
		print ("Su asistente se iniciara en modo asistente de voz")
		print "ESTE MODO UTILIZA LA API DE BING. NECESITA UNA CUENTA DE ESTE SERVICIO. ES PRIVATIVO, PERO GRATIS"
		print "-------------------------------------------------"
	else:
		sys.exit(0)
	dato.close()

def install_mode():
	stat_datos = leertxtv1("app/stats.txt")
	dato = open ("app/stats.txt","w")
	dato.write(stat_datos[0]+"-"+stat_datos[1]+"-"+stat_datos[2]+"-"+stat_datos[3] + stat_datos[4])
	print "-------------------------------------------------"
	modo = raw_input("En que modo desea iniciar su asistente?(terminal/servidor/voz)")
	if modo == "terminal":
		dato.write("terminal-")
		print (stat_datos[0] + " se iniciara en modo terminal")
		print "-------------------------------------------------"
	elif modo == "voz":
		dato.write("voz-")
		print (stat_datos[0] + " se iniciara en modo asistente de voz")
		print "ESTE MODO UTILIZA LA API DE BING. NECESITA UNA CUENTA DE ESTE SERVICIO. ES PRIVATIVO, PERO GRATIS"
		print "-------------------------------------------------"
	else:
		dato.write("terminal-")
	dato.close()
	print "Si desea cambiar el modo de inicio por defecto, por favor utilice setup.py mode"
	print "-------------------------------------------------"


def api():
	print "-------------------------------------------------"
	print "Rellene los datos a continuacion sobre su Asistente Personal"
	print "-------------------------------------------------"
	nombre_apiai = raw_input("API.AI: Token de acceso: ")
	print "-------------------------------------------------"
	key_apiai = raw_input("API.AI: Key: ")
	print "-------------------------------------------------"
	nombre_bing = raw_input("Bing Speech: ID del usuario: ")
	print "-------------------------------------------------"
	key_bing = raw_input("Bing Speech: Key: ")
	print "-------------------------------------------------"
	stat_datos = leertxtv2("app/api.txt")
	dato = open ('app/api.txt','w')
	dato.write(nombre_apiai+"+_+"+key_apiai+"+_+"+nombre_bing+"+_+"+key_bing+"+_+"stat_datos[4])
	dato.close()

def create_server():
	print "-------------------------------------------------"
	nub = raw_input ("Desea habilitar el modo servidor para su uso? (Solo red local) [S/N]")
	print "-------------------------------------------------"
	print "-------------------------------------------------"
	if nub == "S" or nub == "s":
		pass
	else:
		sys.exit(0)
	inicio = os.getcwd()
	os.chmod("etc/hosts",0777)
	file = open("etc/hosts","r")
	texto = file.read()
	file.close()
	file_trans = open("hosts","a")
	file_trans.write("127.0.0.1      igor_web\n")
	file_trans.write(texto)
	file_trans.close()
	file_wr = open("igor-web.conf","r")
	file_wr.write("<VirtualHost *:80>\n  ServerName igor-web\n  DocumentRoot " + inicio + "/html\n  WSGIScriptAlias / "+ inicio +"/app/controller.py\n  ErrorLog " + inicio + "/logs/errors.log\n  CustomLog " + inicio + "/logs/access.log combined\n <Directory "+inicio+"/app>\n  <Files controller.py>\n  Require all granted\n  </Files>\n  </Directory>\n</VirtualHost>")
	os.system("sudo cp -f hosts /etc")
	os.system("sudo cp -f igor_web.conf /etc/apache2/sites-available")
	os.system("sudo cp -f 000-default.conf /etc/apache2/sites-available")
	os.system("sudo a2ensite igor_web")
	os.system("sudo service apache2 restart")
	print "-------------------------------------------------"
	print "Servidor Igor_AI activo. Puede acceder desde http://localhost desde cualquier dispositivo de su red"
	print "-------------------------------------------------"
	nub1 = raw_input ("Desea habilitar el modo servidor web para su uso? (Online)(Basado en Pagekite) [S/N]")
	print "-------------------------------------------------"
	print "-------------------------------------------------"
	if nub1 == "S" or nub1 == "s":
		pass
	else:
		sys.exit(0)
	os.system("sudo python app/lib/pagekite.py --signup")




