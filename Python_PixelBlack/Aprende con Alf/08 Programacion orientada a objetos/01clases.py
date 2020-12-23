#Vamos a crear la clase silla

#Una clase es un constructor de objetos.
class claseSilla:
    color = 'Blanco'
    precio = 100
#Ahora vamos a crear un objeto
objetoSilla=claseSilla()
print(objetoSilla.color) #si lo ejecutamos, vemos que el color es el mencionado.

#ahora creamos otro objeto silla y en este caso, le vamos a cambiar atributos.
objetoSilla2=claseSilla()
objetoSilla2.color='Verde'
objetoSilla2.precio=120
print(objetoSilla2.color, objetoSilla2.precio)

#ahora vamos a crear la clase persona, pero vamos a pedir su nombre y edad en la propia función
class persona:
    def __init__(self,nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def saludar(self):
        print('Hola, me llamo {} y tengo {} años'.format(self.nombre, self.edad))

persona1=persona('Dani',30)
persona1.saludar()