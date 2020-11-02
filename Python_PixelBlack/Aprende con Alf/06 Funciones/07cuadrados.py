'''
Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.
'''

def cuadrados(lista):
    cuadrados=[]
    for i in lista:
        cuadrados.append(i**2)
    return cuadrados
lista=[]
for i in range(10):
    lista.append(float(input('Introduce un nuevo valor ({0}): '.format(i+1))))

print(cuadrados(lista))