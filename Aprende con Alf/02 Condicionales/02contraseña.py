'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por 
la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.
'''

password='contraseña'.lower()
pass_user=input('Introduce la contraseña: ').lower() #almaceno la contraseña del usuario directamente en minúsculas

#ahora hago el condicional

if password == pass_user:
    print('Contraseña correcta')
else:
    print('Contraseña incorrecta')