import os

f_path='ficheros/ejemplo.txt'
contador = 0
if os.path.exists(f_path):
    fichero=open(f_path,'r')
    for linea in fichero:
        if linea[-1] == '\n':
            print(linea[:-1])
        else:
            print(linea)
        contador += 1
    print('En total tenemos', contador, 'lineas en este fichero.')
    fichero.close()
else:
    print('El fichero no existe.')

