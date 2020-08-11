# Importar librerias de sistema
#----------------------------------------------------
#----------------------------------------------------

import sys
import io
import os

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

if sys.argv[1] == "online":
    os.system("sudo python app/lib/pagekite.py &")
else:
	os.system("sudo python app/igor_ai.py")
