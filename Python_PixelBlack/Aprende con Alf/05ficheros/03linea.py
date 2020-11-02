'''
Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con la tabla de multiplicar de ese número,
y muestre por pantalla la línea m del fichero. Si el fichero no existe debe mostrar un mensaje por pantalla informando de ello.
'''
n = int(input('Introduce la tabla a consultar: '))
m = int(input('Introduce el línea a consultar: '))
f=open('D:\Documentos\Github\Python_PixelBlack\Aprende con Alf/05ficheros/tablas-{0}.txt'.format(n),'r')
try:
    a=f.readlines()
    print(a[m-1])

except:
    print('El fichero no existe. IMBÉCIL.')

f.close()