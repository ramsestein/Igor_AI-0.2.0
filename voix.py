# Importar librerias de sistema
#----------------------------------------------------
#----------------------------------------------------

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

def reinstall_voices():
	print "Voces instalables para Igor_AI:"
	print "Male1-9/Female1-7"
	loop = True
	while loop == True:
		value = raw_input("Desea probar alguna de las voces? (Male1-9/Female1-9/No): ")
		if value == "Male1" or value == "male1":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male one' -voice aew")
		elif value == "Male2" or value == "male2":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male two' -voice ahw")
		elif value == "Female1" or value == "female1":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz female one' -voice aup")
		elif value == "Male3" or value == "male3":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male three' -voice awb")
		elif value == "Female2" or value == "female2":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz female two' -voice axb")
		elif value == "Male4" or value == "male4":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male four' -voice bdl")
		elif value == "Female3" or value == "female3":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz female three' -voice clb")
		elif value == "Female4" or value == "female4":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz female four' -voice eey")
		elif value == "Male5" or value == "male5":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male five' -voice fem")
		elif value == "Male6" or value == "male6":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male six' -voice gka")
		elif value == "Male7" or value == "male7":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male seven' -voice jmk")
		elif value == "Male8" or value == "male8":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male eight' -voice ksp")
		elif value == "Female2" or value == "female5":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz female five' -voice ljm")
		elif value == "Male9" or value == "male9":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz male nine' -voice rms")
		elif value == "Female6" or value == "female6":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz female six' -voice rxr")
		elif value == "Female7" or value == "female7":
			os.system("./app/lib/mimic/bin/mimic -t 'Prueba de voz female seven' -voice slt")
		elif value == "No" or value == "no":
			loop = False

	loop = True
	stat_datos = leertxtv1("app/stats.txt")
	dato = open ('app/stats.txt','w')
	dato.write(stat_datos[0]+"-"+stat_datos[1]+"-"+stat_datos[2]+"-"+stat_datos[3])

	while loop == True:
		value = raw_input("Desea instalar alguna de las voces? (Male1-9/Female1-9/No): ")
		if value == "Male1" or value == "male1":
			dato.write("voice voices/cmu_us_aew.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male1"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male2" or value == "male2":
			dato.write("voice voices/cmu_us_ahw.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male2"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Female1" or value == "female1":
			dato.write("voice voices/cmu_us_aup.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Female1"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male3" or value == "male3":
			dato.write("voice voices/cmu_us_awb.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male3"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Female2" or value == "female2":
			dato.write("voice voices/cmu_us_axb.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Female2"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male4" or value == "male4":
			dato.write("voice voices/cmu_us_bdl.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male4"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Female3" or value == "female3":
			dato.write("voice voices/cmu_us_cld.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Female3"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Female4" or value == "female4":
			dato.write("voice voices/cmu_us_eey.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Female4"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male5" or value == "male5":
			dato.write("voice voices/cmu_us_fem.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male5"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male6" or value == "male6":
			dato.write("voice voices/cmu_us_gka.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male6"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male7" or value == "male7":
			dato.write("voice voices/cmu_us_jmk.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male7"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male8" or value == "male8":
			dato.write("voice voices/cmu_us_ksp.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male8"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Female5" or value == "female5":
			dato.write("voice voices/cmu_us_ljm.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Female5"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Male9" or value == "male9":
			dato.write("voice voices/cmu_us_rms.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Male9"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Female6" or value == "female6":
			dato.write("voice voices/cmu_us_rxr.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Female6"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "Female7" or value == "female7":
			dato.write("voice voices/cmu_us_slt.flitevox-" + stat_datos[5])
			dato.close()
			print "Seleccionada voz Female7"
			print "--------------------------------------------------------------"
			loop = False
		elif value == "No" or value == "no":
			print "No se realizan cambios"
			print "--------------------------------------------------------------"
			loop = False


