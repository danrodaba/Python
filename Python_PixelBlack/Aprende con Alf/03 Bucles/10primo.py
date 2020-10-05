'''
Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no.
'''
from time import sleep
n = int(input('Introduce un número entero: '))
x=1
a=1
while x < n-1 and a !=0:
    x+=1
    a=n%x
if a!=0:
    print('El número {0} es primo'.format(n))
elif n%5==0 and n != 5:
    print('¿En serio? ¿Un múltiplo de 5? Voy a pensar 10 segundos por qué no debería darte pantallazo azul...')
    sleep(1)
    print(1, 'segundo')
    for i in range(2,9):
        sleep(1)
        print(i, 'segundos')
    for i in range(1,7):
        sleep(1)
        print('{0:.2f} segundos'.format(9+i/6))
    print('Ahora preguntame por algo que no sepan en primaria, inútil.')
elif n%2==0 and n != 2:
    print('¿Un número par? ¿Me estás preguntando si es primo un número par? ¡¡VETE A LA MIERDA!!')
else:
    print('{0} no es primo porque es, al menos, divisible por {1}'.format(n,x))
