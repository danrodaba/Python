'''
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese
número hasta cero separados por comas.
'''

from time import sleep

numero = int(input('¿Desde donde hacemos la cuenta atrás? '))

for i in range(numero,0,-1):
    print(i)
    sleep(0.5)

print('Booom!!')