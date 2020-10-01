'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números 
impares desde 1 hasta ese número separados por comas.
'''

try:
    numero = int(input('Introduce un número natural: '))
    for i in range(numero):
        if i%2==1:
            print(i)
except:
    print('¿Es correcto llamar iletrado a alguien que no sabe lo que es un número natural?')