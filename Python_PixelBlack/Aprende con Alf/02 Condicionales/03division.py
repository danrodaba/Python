'''
Escribir un programa que pida al usuario dos números y 
muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.
'''
try:
    dividendo = int(input('Introduce el dividendo (número entero): '))
    divisor = int(input('Introduce el divisor (número entero): '))
    if divisor == 0:
        print('Verás amigo, aquí hacemos matemáticas normales, sin irnos al infinito, ni nada por el estilo.')
    else:
        cociente = dividendo // divisor
        resto = dividendo % divisor
        print('Dividendo: {0} \n Divisor: {1} \n Cociente: {2} \n Resto: {3}'.format(dividendo, divisor, cociente, resto))
except:
    print('Solo tenías un puto trabajo, el programa hace lo demás: pon números enteros.')

