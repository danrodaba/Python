import sys
from PyQt5 import uic
from PyQt5.QtWidgets import * 

class Ventana(QMainWindow):

    datos=[]

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('formulario.ui',self)
        self.btn_aceptar.clicked.connect(self.click_aceptar)
        #self.btn_eliminar.clicked.connect(self.click_eliminar)

    def click_aceptar(self):
        self.datos.append(self.DNI_NIE.text())
        self.datos.append(self.nombre.text())
        self.datos.append(self.apellidos.text())
        self.datos.append(self.direccion.text())
        self.datos.append(self.telefono.text())
        self.datos.append(self.poblacion.text())
        self.datos.append(self.cp.text())
        self.datos.append(self.provincia_cbb.currentText())
        self.datos.append(self.email.text())
        self.datos.append(self.setChecked())
        self.datos.append(self.observaciones.toPlainText())
        print(self.datos)
    #def click_eliminar(self):
        

        


app = QApplication(sys.argv)
miVentana = Ventana()
miVentana.show()
app.exec_()