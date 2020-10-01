#defino las variables
cuenta_ini=3000
salario=1100
gastos=435
cuenta_fin=6000

#ahora defino la función matemática
gastos_extra=(cuenta_fin - cuenta_ini - gastos * 12 + salario * 12)/12

print('Los gastos extra ascienden a ', gastos_extra, '€/mes')