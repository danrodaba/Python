'''
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.
'''

palabro = input('Introduce una palabra: ')

for i in range(10):
    if i%2 ==1:
        print(palabro.upper())
    else:
        print(palabro.lower())