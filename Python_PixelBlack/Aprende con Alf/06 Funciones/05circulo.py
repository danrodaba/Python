'''
Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
'''

def circulo(r):
    from math import pi
    area=pi*r**2
    return area

radio=float(input('Introduce el radio del círculo: '))
print(circulo(radio))

altura = float(input('Introduce la altura del cilíndro: '))
print(circulo(radio)*altura)