'''
Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000€ mensuales.
 Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que 
 tributar o no.
'''

edad = int(input('Introduce tu edad: '))
salario = float(input('Introduce tu salario mensual: '))

if edad <16 or salario <=1000:
    print('No paga el impuesto.')
else:
    print('Afloja...')