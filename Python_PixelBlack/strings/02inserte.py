'''
Crear un programa que lea por teclado una cadena y un carácter, e inserte el carácter entre cada letra de la cadena. 
Ej: separar y , debería devolver s,e,p,a,r,a,r
'''
cadena=input('Introduce una cadena: ')
x=1
CADENA=cadena[0]+', '
while x<len(cadena)-1:
    caracter=cadena[x]
    CADENA+=caracter+', '
    x+=1
CADENA+=cadena[-1]
print(CADENA)