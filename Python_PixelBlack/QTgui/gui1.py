import sys
from PyQt5 import uic
from PyQt5.QtWidgets import * 

class Ventana(QMainWindow):

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('gui1.ui',self)
        self.aceptar.clicked.connect(self.click_btn_aceptar)
        self.salir.clicked.connect(self.click_btn_salir)
        self.cancelar.clicked.connect(self.click_btn_cancelar)

    def click_btn_aceptar(self):
        self.Respuesta.setText('Has aceptado el formulario. ')

    def click_btn_salir(self):
        if QMessageBox.question(self, 'Aplicación','¿Desea salir?') == QMessageBox.Yes:
            self.close()
    
    def click_btn_cancelar(self):
        self.txt_nombre.clear()
        self.txt_contrasena.clear()

app = QApplication(sys.argv)
miVentana = Ventana()
miVentana.show()
app.exec_()