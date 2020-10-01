'''
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10.
'''
for i in range(1,11):
    print('Tabla del {0}'.format(i))
    for j in range(1,11):
        print('{0} · {1} = {2}'.format(i,j,i*j))