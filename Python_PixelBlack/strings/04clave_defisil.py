'''
Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos los espacios por el carácter. 
Ej: mi archivo de texto.txt y _ debería devolver mi_archivo_de_texto.txt
'''

clave = input('Introduce tu clave: ')
Clave = 'Tu clave es: {0}'.format(clave)
print(Clave.replace(clave,'X'*len(clave)))