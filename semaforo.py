lectura=int(input('Ponlo por texto porque no tienes un lector (1,2 o 3): '))

if lectura == 1:
    print('Avanza')
elif lectura == 3:
    print('Detente')
elif lectura == 2:
    print('Avanza si no te da tiempo a detenerte')
else:
    print('¿Qué no has entendido de "(1,2 o 3)"?, ¡Gelipoyo!')