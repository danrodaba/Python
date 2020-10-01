'''
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.
'''
eco=input('Háblame y te copio ("salir" para finalizar): ').lower()
while eco != 'salir':
    print(eco)
    eco=input('Háblame y te copio ("salir" para finalizar): ').lower()