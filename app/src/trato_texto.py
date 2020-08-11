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

#leertxt("stats.txt")