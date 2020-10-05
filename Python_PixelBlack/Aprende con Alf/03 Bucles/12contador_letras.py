'''
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de 
veces que aparece la letra en la frase.
'''

frase = input('Introduce tu frase: ').lower()
letra = input('¿Qué letra eliges? ').lower()
while len(letra)!=1:
    letra = input('Sólo una letra. ¿Qué letra eliges? ').lower()
x=0
for i in range(len(frase)):
    if frase[i] == letra:
        x+=1
print('La letra {0} aparece {1} veces en la frase.'.format(letra,x))