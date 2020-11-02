'''
Escribir una función que pida un número entero entre 1 y 10 y guarde en un fichero con el nombre tabla-n.txt 
la tabla de multiplicar de ese número, done n es el número introducido.
'''

n=int(input('Introduce un número natural: '))
f=open('D:\Documentos\Github\Python_PixelBlack\Aprende con Alf/05ficheros/tablas-{0}.txt'.format(n),'w')
for i in range(1,11):
    resultado='{0} x {1} = {2}'.format(i,n,i*n)
    print(resultado)
    f.write(resultado)
    f.write('\n')
f.close()