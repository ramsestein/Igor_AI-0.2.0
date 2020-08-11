# Importar librerias de sistema
#----------------------------------------------------
#----------------------------------------------------

import sys
import io
import os
import ins
import voix
import mode

if sys.argv[1] == "install" or sys.argv[1] == "-i":
	ins.install()
	mode.api()
	ins.reinstall_corpus()
	mode.install_mode()
	mode.create_server()
elif sys.argv[1] == "reinstall_corpus" or sys.argv[1] == "-ric":
	ins.reinstall_corpus()
elif sys.argv[1] == "mode" or sys.argv[1] == "-m":
	try:
		mode.mode(sys.argv[2])
	except:
		mode.mode(" ")
elif sys.argv[1] == "help" or sys.argv[1] == "-h":
	ins.help()
elif sys.argv[1] == "api" or sys.argv[1] == "-a":
	mode.api()
elif sys.argv[1] == "reinstall_voices" or sys.argv[1] == "-riv":
	voix.reinstall_voices()
elif sys.argv[1] == "create_server" or sys.argv[1] == "-cr":
	mode.create_server()
else:
	ins.install()
	mode.api()
	ins.reinstall_corpus()
	mode.install_mode()
	mode.create_server()
