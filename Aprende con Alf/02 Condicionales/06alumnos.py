'''
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre 
posterior a la N y el grupo B por el resto. Escribir un programa que pregunte al usuario su nombre y sexo,
y muestre por pantalla el grupo que le corresponde.
'''

nombre = input('Introduce el nombre: ')
inicial= nombre[0].lower()
sexo = 'Holi'
while sexo.lower() != 'hombre' and sexo.lower() != 'mujer':
    sexo=input('Introduce su sexo (hombre o mujer): ').lower()
if sexo == 'mujer' and inicial < 'm' or (sexo == 'hombre' and inicial > 'm'):
    print('Grupo A')
else:
    print('Grupo B')

print('El sistema de clasificación más innecesariamente complejo del día.')