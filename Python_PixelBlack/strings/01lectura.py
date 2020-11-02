'''
1.	Crear un programa que lea por teclado una cadena, y muestre la siguiente información:
Imprima los dos primeros caracteres.
Imprima los tres últimos caracteres.
Imprima dicha cadena cada dos caracteres. Ej.: recta debería imprimir rca
Dicha cadena en sentido inverso. Ej.: hola mundo! debe imprimir !odnum aloh
Imprima la cadena en un sentido y en sentido inverso. Ej: reflejo imprime reflejoojelfer.

'''
cadena = input('Introduce una cadena de texto: ')
print(cadena[0:2])
print(cadena[-4:-1])
print(cadena[0:-1:2])
print(cadena[::-1])
anedac=cadena[::-1]
print(cadena+anedac)