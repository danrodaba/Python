'''
Escribir una función que reciba una muestra de números en una lista y devuelva su media.
'''
def media(lista):
    promedio=sum(lista)/len(lista)
    return promedio
lista=[]
for i in range(10):
    lista.append(float(input('Introduce un nuevo valor ({0}): '.format(i+1))))

print(media(lista))