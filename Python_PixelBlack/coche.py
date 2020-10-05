def gasto(dias):

    #defino variables
    consumo=5.5/100
    distancia=15
    precio=1.12
    viajes_dia=2

    #defino función matemática
    return consumo*distancia*precio*dias*viajes_dia

#ahora pido que me imprima por pantalla el resultado
a=int(input('¿Durante cuántos días? '))
gasto_total=gasto(a)
print('En',a ,'días gastarás ',gasto_total,'€')