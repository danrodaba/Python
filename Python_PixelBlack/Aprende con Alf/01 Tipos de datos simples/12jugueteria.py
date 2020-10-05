clown=112
doll=75

n_clown=int(input('¿Cuántos payasos van? '))
n_doll=int(input('¿Cuantas muñecas van?' ))

masa=n_clown*clown + n_doll * doll

print('La masa total del envío es {0}kg.'.format(masa/1000))