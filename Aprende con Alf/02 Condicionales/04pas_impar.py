'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.
'''
try:
    numero = int(input('Introduce un número entero: '))
    if numero%2==0:
        print('{0} es par'.format(numero))
    else:
        print('{0} es impar'.format(numero))
except:
    print('"Entero" del verbo enterar, no como tú.')