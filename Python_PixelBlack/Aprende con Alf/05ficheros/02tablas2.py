'''
Escribir una función que pida un número entero entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
 done n es el número introducido, y la muestre por pantalla. Si el fichero no existe debe mostrar un mensaje por pantalla informando
 de ello.
'''

n=int(input('Introduce un número natural: '))
f=open('D:\Documentos\Github\Python_PixelBlack\Aprende con Alf/05ficheros/tablas-{0}.txt'.format(n),'r')
try:
    a=f.readlines()
    for i in a:
        print(i,end='')

except:
    print('El fichero no existe. IMBÉCIL.')

f.close()