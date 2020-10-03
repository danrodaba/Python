'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. 
Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''

subjects=['Matemáticas','Física','Química','Historia','Lengua']
notas=[]
passed = []
for i in range(len(subjects)):
    notas.append(float(input('¿Qué nota has sacado en {0}? '.format(subjects[i]))))
    if notas[i] >= 5:
        passed.append(subjects[i])
for i in range(len(passed)):
    subjects.remove(passed[i])
print(subjects)