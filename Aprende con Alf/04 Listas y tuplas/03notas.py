'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua)
 en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
 En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las 
 correspondientes notas introducidas por el usuario.
'''


subjects=['Matemáticas','Física','Química','Historia','Lengua']
notas=[]
for i in subjects:
    notas.append(float(input('¿Qué nota has sacado en {0}? '.format(i))))
for i in range(len(subjects)):
    print('Has sacado un {0} en {1}'.format(notas[i], subjects[i]))