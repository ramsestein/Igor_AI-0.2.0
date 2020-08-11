# Igor_AI-0.2.0

--------------------------------------------------------
Instalación:
--------------------------------------------------------
Introducir en la terminal lo siguientes comandos:

$ tar -xzvf Igor_AI-0.1.tar.gz
$ cd Igor_AI-0.1
$ sudo python setup.py install

Si se desean cambiar los Corpus de entrenamiento, de deberán cambiar en las carpetas de "data" segun correspondan. Posteriormente ejecutar

$ sudo python setup.py reinstall_corpus

En la carpeta lib se encuentran las librerias que se instalaran via setup.py, en caso de error, instalar manualmente
--------------------------------------------------------
Iniciar Igor_AI:
--------------------------------------------------------
Introducir en la terminal el siguiente comando en terminal, dentro de la carpeta del asistente

$ ./start.py

ó

$ python start.py 
--------------------------------------------------------
Modos de arranque en Igor_AI:
--------------------------------------------------------
Durante la instalacion se deberá escoger el modo en el que se inicia el servicio. Existiendo tres modos escogibles:

	- Terminal: Modo texto escrito a traves de terminal. Modo de depuración por excelencia para los nuevos modulos que el usuario deseara añadir

	- Servidor: #########
	
	- Voz: Utilizando Mimic y Bing Speech. Modo asistente de voz por excelencia. Nota: Bing Speech es un servicio privativo aunque gratuito, necesita que el usuario tenga una cuenta activa para el mismo. Se ha utilizado a falta de otra alternativa viable
--------------------------------------------------------
Voces en Igor_AI:
--------------------------------------------------------
Igor_AI utiliza Mimic para su propia voz, software provisto por Mycroft y VocaliD.

Las voces en Igor_AI se encuentran dentro de la carpeta lib/mimic/voices. 

En caso de añadirse un nuevo archivo de voz, queriendo usar este para la voz de su asistente, deberá sustituirse el nombre y extensión de este archivo en el archivo stats.txt en el lugar correspondiente, en la quinta posición, manualmente
--------------------------------------------------------
APIs en Igor_AI:
--------------------------------------------------------
Igor_AI utiliza las APIs de API.AI y de Bing, siendo esta ultima de uso exclusivo para el sistema de voz.

Ambos servicios son gratuitos y no requieren más configuración que su mera creación. El cambio de las credenciales son obligatorias.

Se adjuntan las web de los servicios:
	- Bing Speech: https://www.microsoft.com/cognitive-services/en-us/speech-api
	- API.AI: https://api.ai/ 
--------------------------------------------------------
--------------------------------------------------------
Carpetas en Igor_AI:
--------------------------------------------------------
app -> Carpeta central de actividad en Igor_AI
|
-->
	lib --> Contiene las librerias que deben trabajarse durante la instalación de Igor_AI. Las dependencias que deben aplicarse son:
		- biopython
		- future
		- mimic
		- numpy
		- pyaudio (Necesariamente >0.2.9)
		- pymongo
		- requests
		- scipy
	No localizadas en lib:
		- sox
		- mongodb-org
		- libasound2-dev
		- gcc
	Las siguientes librerías también son necesarias pero han sido modificadas para Igor_AI, debiendose instalarse obligatoriamente desde lib:
		- ChatterBot
		- Api-AI

	busq --> Contendrá los archivos con los logs de las busquedas en pudmed

	src --> Contiene los módulos para acciones de Igor sobre el sistema. Igor puede realizar las siguientes acciones:
		- Abrir archivos (usando el programa por defecto)
		- Abrir programas
		- Borrar archivos
		- Borrar carpetas
		- Copiar archivos
		- Copiar carpetas
		- Crear archivos
		- Crear carpetas

	data --> Contenedor de los corpus que se reinstalarían con el comando 'reinstall_corpus'
	
	med --> Contiene los módulos para acciones de Igor de tipo 	sanitarias. Igor puede realizar las siguientes acciones:
		- Buscar datos en Gene y Protein

html --> Datos web contenidos para el servidor Igor_AI

logs --> Errores e incidencias recogidas por el servidor
--------------------------------------------------------
Errores Igor_AI:
--------------------------------------------------------
- Error: Modo Sin Entrenamiento ON
	*Iniciar programa como superusuario (sudo)

- Error: Error al instalar manualmente api-ai desde la carpeta lib
	*El archivo setup.py está modificado para el instalador, en las linea 30 y 33 del archivo se debera sustituir:
	"with open('lib/api-ai-python-master/README.rst', 'r') as f:" y
	"with open('lib/api-ai-python-master/HISTORY.rst', 'r') as f:"
	por:
	"with open('README.rst', 'r') as f:"
	"with open('HISTORY.rst', 'r') as f:"
	
	
