import random

texto=input('Introduce tu texto: ').lower()

alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ']
codigo=[]
n=1

#ahora voy a crear el código, que se genera aleatoriamente asignando un número a cada letra.
while n<=28:
  letra=random.randint(1,28)
  if letra <10:
    letra='0'+str(letra)
  else:
    letra=str(letra)
  while letra not in codigo:
    codigo.append(str(letra))
    n+=1
diccionario=dict(zip(alfabeto,codigo))
print(diccionario)
#en este bloque el texto es reemplazado
for i in range(len(codigo)):
  texto=texto.replace(alfabeto[i],codigo[i])
print('Texto encriptado.')
print(texto)
print('Tu código es: {0}'.format(''.join(codigo)))