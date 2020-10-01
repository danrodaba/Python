precio = 3.49
descuento = 0.6
ventas = int(input('¿Cuántas barras del día anterior se han vendido? '))

print('Precio habitual: {0}€ \n Descuento: {1:.0f}% \n coste final: {2:.2f}€'.format(precio*ventas,descuento*100,ventas*(1-descuento)*precio))