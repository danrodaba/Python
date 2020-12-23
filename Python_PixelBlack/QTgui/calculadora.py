import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from math import pi, e, log

class Calculadora(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('calculadora.ui',self)
        self.resultado = ''
        self.operacion = ''
        self.valor1 = '0'
        self.valores.setText('0')

        #botones números
        self.cero.clicked.connect(self.click_cero)
        self.uno.clicked.connect(self.click_uno)
        self.dos.clicked.connect(self.click_dos)
        self.tres.clicked.connect(self.click_tres)
        self.cuatro.clicked.connect(self.click_cuatro)
        self.cinco.clicked.connect(self.click_cinco)
        self.seis.clicked.connect(self.click_seis)
        self.siete.clicked.connect(self.click_siete)
        self.ocho.clicked.connect(self.click_ocho)
        self.nueve.clicked.connect(self.click_nueve)
        self.coma.clicked.connect(self.click_coma)
        self.pi.clicked.connect(self.click_pi)
        self.exp.clicked.connect(self.click_exp)

        #operaciones
        self.suma.clicked.connect(self.click_suma)
        self.resta.clicked.connect(self.click_resta)
        self.multiplicacion.clicked.connect(self.click_multiplicacion)
        self.division.clicked.connect(self.click_division)
        self.potencia.clicked.connect(self.click_potencia)
        self.igual.clicked.connect(self.click_igual)
        self.raiz_cuadrada.clicked.connect(self.click_raiz_cuadrada)
        self.inversa.clicked.connect(self.click_inversa)
        self.neperiano.clicked.connect(self.click_neperiano)
        self.abs.clicked.connect(self.click_abs)
        self.CE.clicked.connect(self.click_CE)
        self.C.clicked.connect(self.click_C)
        self.borrar.clicked.connect(self.click_borrar)

        #escribir número en pantalla

        #operaciones
    
    def escribe_numero(self,numero):
        salida=self.valores.toPlainText() + numero
        self.valores.setText(salida)
        print(self.valores)
    def click_cero(self):
        self.escribe_numero('0')
    def click_uno(self):
        self.escribe_numero('1')
    def click_dos(self):
        self.escribe_numero('2')
    def click_tres(self):
        self.escribe_numero('3')
    def click_cuatro(self):
        self.escribe_numero('4')
    def click_cinco(self):
        self.escribe_numero('5')
    def click_seis(self):
        self.escribe_numero('6')
    def click_siete(self):
        self.escribe_numero('7')
    def click_ocho(self):
        self.escribe_numero('8')
    def click_nueve(self):
        self.escribe_numero('9')
    def click_coma(self):
        if self.valores.toPlainText().find('.') == -1:
            self.escribe_numero('.')
    def click_pi(self):
        self.escribe_numero(str(pi))
    def click_exp(self):
        self.escribe_numero(str(e))
    #click operaciones

    def click_suma(self,numero):
        self.valor1=float(self.valores.toPlainText())
        self.valores.setText('')
        salida = str(self.valores.toPlainText())
        self.valores.setText(salida)
        self.operacion='suma'

    def click_resta(self,numero):
        self.valor1=float(self.valores.toPlainText())
        self.valores.setText('')
        salida = str(self.valores.toPlainText())
        self.valores.setText(salida)
        self.operacion='resta'

    def click_multiplicacion(self,numero):
        self.valor1=float(self.valores.toPlainText())
        self.valores.setText('')
        salida = str(self.valores.toPlainText())
        self.valores.setText(salida)
        self.operacion='multiplicación'

    def click_division(self,numero):
        self.valor1=float(self.valores.toPlainText())
        self.valores.setText('')
        salida = str(self.valores.toPlainText())
        self.valores.setText(salida)
        self.operacion='division'

    def click_potencia(self,numero):
        self.valor1=float(self.valores.toPlainText())
        self.valores.setText('')
        salida = str(self.valores.toPlainText())
        self.valores.setText(salida)
        self.operacion='potencia'
    #otras operaciones
    def click_raiz_cuadrada(self,valor1):
        self.resultado = str((float(self.valores.toPlainText()))**(1/2))
    def click_inversa(self,valor1):
        self.resultado = str(1/float(self.valores.toPlainText()))
    def click_neperiano(self,valor1):
        self.resultado = str(log(float(self.valores.toPlainText())))
    def click_abs(self,valor1):
        self.resultado = str(abs((float(self.valores.toPlainText()))))
    def click_C(self):
        self.resultado = '0'
        self.valor1 = '0'
        self.valor2 = '0'
        self.valores.setText('0')
    def click_CE(self):
        self.valores.setText('0')
    def click_borrar(self):
        self.valores=self.valores[:-1] #no funciona


    #igual (=)
    def click_igual(self,valor1):
        self.valor2 = float(self.valores.toPlainText())
        if self.operacion == 'suma':
            self.resultado=str(self.valor1 + self.valor2)
        elif self.operacion == 'resta':
            self.resultado=str(self.valor1 - self.valor2)
        elif self.operacion == 'multiplicación':
            self.resultado=str(self.valor1 * self.valor2)
        elif self.operacion == 'division':
            self.resultado = str(self.valor1 / self.valor2)
        elif self.operacion == 'potencia':
            self.resultado = str(self.valor1 ** self.valor2)
        
        #en este if, le retiro los decimales si son irrelevantes
        if self.resultado[-2:]=='.0':
            self.resultado=self.resultado[:-2]
        self.valores.setText(self.resultado)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    miVentana = Calculadora()
    miVentana.show()
    app.exec_()