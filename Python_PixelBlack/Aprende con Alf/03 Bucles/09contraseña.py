'''
Escribir un programa que almacene la cadena de caracteres contraseña en una variable, 
pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.'''

password='contraseña'
password=password.lower()
user_pass=input('Introduce tu contraseña: ').lower()
while user_pass != password:
    user_pass=input('Contraseña incorrecta. Introduce tu contraseña: ').lower()
print('Contraseña correcta')