'''
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a una las letras de la palabra
introducida empezando por la última.
'''

palabro=input('Introduce una palabra: ').upper()
if ' ' in palabro:
    print('Solo una palabra')
else:
    for i in range(len(palabro)):
        print(palabro[len(palabro)-i-1])