'''
Vamos a introducir una serie de 3 elementos numéricos y a obtener de ellos el promedio
'''
#entrada de variables.
try:
    tienda1=float(input('Introduce el precio de la primera tienda: '))
    tienda2=float(input('Introduce el precio de la segunda tienda: '))
    tienda3=float(input('Introduce el precio de la segunda tienda: '))
except:
    print('No me seas letrasado, ponla como un número')

#operaciones
promedio=(tienda1+tienda2+tienda3)/3

#imprimimos resultados
print('En promedio, el producto cuesta sobre {:0.2f}€'.format(promedio))