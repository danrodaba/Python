'''
Crear un programa que lea por teclado una cadena y un carácter, y reemplace todos los espacios por el carácter.
Ej: mi archivo de texto.txt y _ debería devolver mi_archivo_de_texto.txt
'''
cadena = input('Introduce una cadena de texto: ')

CADENA=cadena.replace(' ','_')
print(CADENA)