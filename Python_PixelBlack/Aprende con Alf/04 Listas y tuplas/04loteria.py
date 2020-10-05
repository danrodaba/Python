'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los 
muestre por pantalla ordenados de menor a mayor.
'''
numeros=[]
for i in range(6):
    x=0
    while x > 49 or x < 1:
        x = int(input('Introduce el numero {0}: '.format(i+1)))
        numeros.append(x)
numeros.sort()
print(numeros)