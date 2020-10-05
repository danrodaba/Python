'''
En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación 
comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados 
pueden ser 0.0, 0.4, 0.6 o más, pero no valores intermedios entre las cifras mencionadas (ole tu papo, si produces 0.3 · 2400
no tienes cabida en la empresa: QUE LES CORTEN LA CABEZA!!!. A continuación se muestra una tabla con los niveles correspondientes
a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.

Nivel	Puntuación
Inaceptable	0.0
Aceptable	0.4
Meritorio	0.6 o más

Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que 
recibirá el usuario.
'''


print('Adelante con la siguiente sandez!!')

calificacion=float(input('Introduce un rendimiento (como el caballo está barato de cojones en esta empresa, solo existen 3 rendimientos: \n 0.0, 0.4 y 0.6 o más, si te sales de ahí, guillotina): '))

if calificacion == 0.0:
    rendimiento='Inaceptable, no como este sistema random de evaluación'
elif calificacion == 0.4:
    rendimiento='Aceptable'
elif calificacion >=0.6:
    rendimiento = 'Meritorio. Oh genio de la empresa, idea un sistema que no nos haga parecer imbéciles!'
else:
    print('Mierda, esa calificación no puede existir!! ¿Se puede provocar un pantallazo azul desde Python?')

print('Rendimiento {}, {}€ producidos.'.format(rendimiento, calificacion * 2400))