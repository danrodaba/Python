'''Vamos a crear un programa que a partir de nuestra fecha de nacimiento nos devuelva nuestra edad.
Para ello, necesitamos la fecha actual y la fecha de nacimiento.
'''

import datetime
#Aquí añadimos una librería ya existente que no viene por defecto. Esto es una de las ventajas de Python: hay mucho código ya diseñado

def edad(birthday):    #def define que empezaremos una función. Despues pondremos pondremos entre paréntesis los parámetros que nos va a pedir.

    hoy = datetime.datetime.today()
#Aquí llamamos a una de las funciones. La sintaxis es "nombre_de_librería.funcion". En este caso parece tener una subcategoría que también se llama datatime'''

    return hoy.year - birthday
'''return nos da el resultado que la función devolverá'''

'''Ahora la tabulación desaparece, de modo que vuelvo a estar fuera de la función "edad" que acabamos de crear.'''

mi_edad = edad(1990)

'''Así llamo a la función. En este caso edad(1990), introduce el argumento '1990' 
a la función edad, y llama 'mi_edad' al resultado.'''

print('Tengo ',mi_edad,' años')

