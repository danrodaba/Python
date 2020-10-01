def miles2meters():
    
    milla=1609.344
    pie=0.3042
    pulgada=2.54

    millas=float(input('¿Cuantas millas son? '))
    pies=float(input('¿Cuantos pies son? '))
    pulgadas=float(input('¿Cuantas pulgadas son? '))

    metros=millas*milla+pies*pie+pulgada*pulgadas
    print('La longitud especificada equivale a {0} metros.'.format(metros))
miles2meters()