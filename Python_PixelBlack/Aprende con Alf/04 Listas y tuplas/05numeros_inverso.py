'''
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
'''

numeros = [x for x in range(1,11)]
numeros.reverse()
for i in range(9):
    print(numeros[i],end=', ')
print(numeros[-1])