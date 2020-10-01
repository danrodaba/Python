inversion = float(input('¿Cuánto quieres invertir?' ))
interes = float(input('¿Cuál es el interés anual? '))/100
tiempo = float(input('¿A cuanto tiempo? '))

capital_total = inversion*(1+interes)**tiempo
print('El capital total asciende a {:.2f}€'.format(capital_total))