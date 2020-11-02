'''
Escribir una función que muestre por pantalla el saludo ¡Hola amiga! cada vez que se la invoque.
'''
def hola(name):
    print('Hola {0}!'.format(name))
    return
nombre = input('Introduce tu nombre: ')
hola(nombre)