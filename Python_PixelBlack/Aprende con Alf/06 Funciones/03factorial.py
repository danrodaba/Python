'''
Escribir una función que reciba un número entero positivo y devuelva su factorial.
'''

def fact(n):
    aux=1
    for i in range(n,1,-1):
        aux*=i
    return(aux)

n=int(input('Introduce un número natural: '))
print(fact(n))