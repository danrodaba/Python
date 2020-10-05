'''
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
'''

edad = int(input('Introduce tu edad: '))
print('Has cumplido todos estos años:')
for i in range(edad):
    print(i+1)

print('Felicidades, Matusalén. Pronto ya no estarás con nosotros.')