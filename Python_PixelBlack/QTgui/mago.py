import sys
from PyQt5 import uic
from PyQt5.QtWidgets import * 



class FichaMago(QMainWindow):
    #enorme batería de variables:
    NOMBRE = ''
    JUGADOR = ''
    CRONICA = ''
    NATURALEZA = ''
    CONDUCTA = ''
    ESENCIA = ''
    AFILIACION = ''
    SECTA = ''
    CONCEPTO = ''
    FUERZA = ''
    DESTREZA = ''
    RESISTENCIA = ''
    CARISMA = ''
    MANIPULACION = ''
    APARIENCIA = ''
    PERCEPCION = ''
    INTELIGENCIA = ''
    ASTUCIA = ''

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('mago.ui', self)
        self.btn_crear.clicked.connect(self.crear_ficha)

    def crear_ficha(self):
        if self.master_modo.isChecked() == False:
            self.NOMBRE = self.nombre.text()
            self.JUGADOR = self.jugador.text()
            self.CRONICA = self.cronica.text()
            self.NATURALEZA = self.naturaleza.text()
            self.CONDUCTA = self.conducta.text()
            self.ESENCIA = self.esencia.text()
            self.AFILIACION = self.afiliacion.text()
            self.SECTA = self.secta.text()
            self.CONCEPTO = self.concepto.text()
            self.FUERZA = self.spinFuerza.value()
            self.DESTREZA = self.spinDestreza.value()
            self.RESISTENCIA = self.spinResistencia.value()
            self.CARISMA = self.spinCarisma.value()
            self.MANIPULACION = self.spinManipulacion.value()
            self.APARIENCIA = self.spinApariencia.value()
            self.PERCEPCION = self.spinPercepcion.value()
            self.INTELIGENCIA = self.spinInteligencia.value()
            self.ASTUCIA = self.spinAstucia.value()
            self.dict_identificacion = {'Nombre' : self.NOMBRE, 'Jugador' : self.JUGADOR, 'Crónica' : self.CRONICA, 'Naturaleza' : self.NATURALEZA, 'Conducta' : self.CONDUCTA, 'Esencia' : self.ESENCIA, 'Afiliación' : self.AFILIACION, 'Secta' : self.SECTA, 'Concepto' : self.CONCEPTO}
            self.identificacion = [self.NOMBRE, self.JUGADOR, self.CRONICA, self.NATURALEZA, self.CONDUCTA, self.ESENCIA, self.AFILIACION, self.SECTA, self.CONCEPTO]
            self.fisicos = [self.FUERZA, self.DESTREZA, self.RESISTENCIA]
            self.sociales = [self.CARISMA, self.MANIPULACION, self.APARIENCIA]
            self.mentales = [self.PERCEPCION, self.INTELIGENCIA, self.ASTUCIA]

            



app = QApplication(sys.argv)
miVentana = FichaMago()
miVentana.show()
app.exec_()