import os

f_path='ficheros/ejemplo.txt'
if os.path.exists(f_path):
    fichero=open(f_path,'r')
    for linea in fichero:
        if linea[-1] == '\n':
            print(linea[:-1])
        else:
            print(linea)
    fichero.close()
else:
    print('El fichero no existe.')