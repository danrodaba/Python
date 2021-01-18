import sys
from PyQt5 import uic
from PyQt5.QtWidgets import * 

class Formulario1(QMainWindow):

    datos=[]

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('formulario.ui',self)
        self.btn_aceptar.clicked.connect(self.click_aceptar)
        self.btn_salir.clicked.connect(self.click_btnCancelar)
        self.btn_limpiar.clicked.connect(self.click_btnLimpiar)

    def click_aceptar(self):        #Al aceptar se imprimirán los resultados como una lista
        self.datos.append(self.DNI_NIE.text())
        self.datos.append(self.nombre.text())
        self.datos.append(self.apellidos.text())
        self.datos.append(self.direccion.text())
        self.datos.append(self.telefono.text())
        self.datos.append(self.poblacion.text())
        self.datos.append(self.cp.text())
        self.datos.append(self.provincia_cbb.currentText())
        self.datos.append(self.email.text())
        self.datos.append(self.cbx_deudor.isChecked())
        self.datos.append(self.cbx_credito.isChecked())
        self.datos.append(self.observaciones.toPlainText())
        if self.rdbtn_hombre.isChecked():
            self.datos.append('hombre')
        elif self.rdbtn_muje.isChecked():
            self.datos.append('mujer')
        elif self.rdbtn_NoBinario.isChecked():
            self.datos.append('no binario')
        print(self.datos)
        self.datos=[]
    
    def click_btnCancelar(self):
        self.close()  # cierra la ventana (luego añadiremos una ventana de confirmación)
    
    def click_btnLimpiar(self):
        self.DNI_NIE.clear()
        self.nombre.clear()
        self.apellidos.clear()
        self.direccion.clear()
        self.telefono.clear()
        self.poblacion.clear()
        self.cp.clear()
        self.provincia_cbb.clear()
        self.email.clear()
        self.cbx_deudor.setChecked(False)
        self.cbx_credito.setChecked(False)
        self.observaciones.clear()
        self.rdbtn_hombre.setChecked(True)
        self.nacimiento.clear()

        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    miVentana = Formulario1()
    miVentana.show()
    app.exec_()