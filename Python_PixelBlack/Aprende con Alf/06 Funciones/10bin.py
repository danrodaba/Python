'''
Escribir una función que convierta un número decimal en binario y otra que convierta un número binario en decimal.
'''
def binario(n):

    lista = []

    while n > 1:
        lista.append(n % 2)
        n//=2
    lista.append(n)
    binario=''
    for i in range(len(lista)):
        binario += str(lista[len(lista)-i-1])
    return binario

print(binario(12))