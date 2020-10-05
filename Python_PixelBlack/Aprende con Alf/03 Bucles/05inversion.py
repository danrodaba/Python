'''
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años,
y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
'''

inversion = float(input('¿Cuánto vas a invertir? '))
interes = float(input('¿A qué interés? '))
tiempo = int(input('¿Cuántos años? '))

for i in range(tiempo):
    capital=inversion*(1+interes/100)**(i+1)
    print('Al final del año {0} tendrás {1}€'.format(i+1,capital))