'''
Escribir un programa para gestionar un listín telefónico con los nombres y los teléfonos de los clientes de una empresa.
El programa incorporar funciones crear el fichero con el listín si no existe, para consultar el teléfono de un cliente, 
añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. El listín debe estar guardado en el fichero de 
texto listin.txt donde el nombre del cliente y su teléfono deben aparecer separados por comas y cada cliente en una línea distinta.
'''

switch=0
opciones = ['Crear listín','Consultar listín','Añadir teléfono','Eliminar teléfono']
while switch not in range(1,5):
    switch = int(input('1) Crear listín \n2) Consultar listín \n3) Añadir teléfono \n4) Eliminar teléfono \n¿Qué deseas hacer (introduce el número del índice)? \n'))

print('Ha seleccionado',opciones[switch-1])
path = 'D:\Documentos\Github\Python_PixelBlack\Aprende con Alf/05ficheros\listin.txt'
if switch == 1:
    f = open(path,'w')
    otro = 'y'
    while otro == 'y':
        nombre = input('Introduce un nuevo nombre: ')
        telefono = input('Introduce el teléfono de {0}: '.format(nombre))
        entrada = nombre + ': ' + telefono + '\n'
        print(entrada)
        f.write(entrada)
        otro = input('Introducirás otra entrada al listín (y/n): ')
elif switch == 2:
    f = open(path,'r')
    contenido = f.readlines()
    for i in contenido:
        print(i,end='')
elif switch == 3:
    f = open(path,'a')
    otro = 'y'
    while otro == 'y':
        nombre = input('Introduce un nuevo nombre: ')
        telefono = input('Introduce el teléfono de {0}: '.format(nombre))
        entrada = nombre + ': ' + telefono + '\n'
        print(entrada)
        f.write(entrada)
        otro = input('Introducirás otra entrada al listín (y/n): ')
elif switch == 4:
    f = open(path,'a')
    contenido=f.readlines()
    for i in contenido:
        print(i)
    borrar = input('¿Qué entrada desea borrar? ')

f.close()