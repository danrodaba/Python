''' Vamos a pedir una nota e imprimir mensajes a traves de una cadena de if'''

#aquí meto un try, por si el usuario no mete un número
try:
    nota = float(input('Introduce la nota: '))
except:
    print('¿Sabes que la nota se entrega como un número, verdad?')

#aquí va la cadena de if

if nota <5:
    print('Suspenso, cazurro')
elif nota <6:
    print('5.gracias, tira')
elif nota <7:
    print('Bien, eres el amo de la mediocridad')
elif nota <9:
    print('Notable')
elif nota <10:
    print('Sobresaliente, un empollón asqueroso')
else:
    print('El profesor a clases de mayes ya')
