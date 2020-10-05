'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de 
pizza aparecen a continuación.

Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre 
un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el 
tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los 
ingredientes que lleva.
'''

vegetarianos = ['Pimiento','Tofu']
no_vegetarianos = ['Peperoni','Jamón','Salmón']

vegetariana = input('¿Quieres que tu pizza sea vegetariana? ').lower()

while vegetariana != 'si' and vegetariana != 'no':
    vegetariana = input('Escribe bien. ¿Quiéres que tu pizza sea vegetariana? ').lower()


if vegetariana == 'si':
    for i in range(len(vegetarianos)):
        menu=vegetarianos
        print(i+1,vegetarianos[i])
if vegetariana == 'no':
    for i in range(len(no_vegetarianos)):
        menu=no_vegetarianos
        print(i+1,no_vegetarianos[i])

numero = int(input('¿Qué ingrediente añadirá a su pizza (introduzca el número)?'))-1

print('El ingrediente elegido es {0}'.format(menu[numero]))