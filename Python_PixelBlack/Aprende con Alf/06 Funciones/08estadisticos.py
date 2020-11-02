'''
Escribir una función que reciba una muestra de números en una lista y devuelva un diccionario con su media, varianza y desviación típica.
'''

def estadisticos(lista):
    media = sum(lista)/len(lista)
    Lvarianza=[]
    for i in range(len(lista)):
        Lvarianza.append((lista[i]-media)**2)
    varianza = sum(Lvarianza)/len(lista)
    desv_est = (sum(Lvarianza)/(len(lista)-1))**(1/2)
    diccionario = {'Media':media,'Varianza':varianza,'Desviación estándar': desv_est}
    return diccionario
lista=[]
for i in range(10):
    lista.append(float(input('Introduce un nuevo valor ({0}): '.format(i+1))))

print(estadisticos(lista))