print('Cálculo de la media de una serie de datos')
print('_________________________________________')

#iniciamos variables
suma=0
n=0

#leemos datos y los procesamos
x=float(input('Introduce un valor a la serie (0para finalizar): '))
while x != 0:
    suma+=x
    n+=1
    x = float(input('Introduce un valor a la serie (0para finalizar): '))
#resultados
print('La media es {}'.format(suma/n))