'''
El fichero cotizacion.csv contiene las cotizaciones de las empresas del IBEX35 con las siguientes columnas: 
Nombre (nombre de la empresa), Final (precio de la acción al cierre de bolsa), Máximo (precio máximo de la acción durante la jornada), 
Mínimo (precio mínimo de la acción durante la jornada), Volumen (Volumen al cierre de bolsa), Efectivo (capitalización al 
cierre en miles de euros).

Construir una función reciba el fichero de cotizaciones y devuelva un diccionario con los datos del fichero por columnas.

Construir una función que reciba el diccionario devuelto por la función anterior y cree un fichero en formato csv con el mínimo,
el máximo y la media de dada columna.
'''

f = open('05ficheros/cotizacion.csv','r',encoding='utf8')

#Con esto saco la cabecera
texto = f.readlines()
cabecera = texto[0][0:-1].split(';')
texto = texto[1:-1]
lista=[]
contador=-1
for line in texto:
    contador+=1
    linea=line[0:-1].split(';')
    iterador_zip=zip(cabecera,linea)
    a=dict(iterador_zip)
    lista.append(a)
    exec(f'entrada{contador}=dict(iterador_zip)') #intento fallido. Cada uno de los diccionarios tiene un nombre.
for i in lista:
    print(i)

f.close()