ahorros = float(input('¿Cuanto dinero has metido a la cuenta? '))
interes = 0.04
year1 = ahorros * (1+interes)**1
year2 = ahorros * (1+interes)**2
year3 = ahorros * (1+interes)**3

print('Los tres primeros años tendrás {0:.2f}€, {1:.2f}€ y {2:.2f}€ respectivamente.'.format(year1,year2,year3))