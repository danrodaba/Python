import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from accesobd import AccesoBD
from mago import FichaMago


class GestorFichas(QMainWindow):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        uic.loadUi('gestor_fichas.ui', self)
        self.showMaximized()
        self.menu()
    
    def menu(self):
        self.actionFicha_Mago.triggered.connect(self.Ficha_mago)
    
    def Ficha_mago(self):
        subVentana = FichaMago()
        self.mdiArea.addSubWindow(subVentana)
        subVentana.show()
        self.mdiArea.tileSubWindows()

if __name__=="__main__":
    #Instancia para iniciar una aplicación    
    app = QApplication(sys.argv)
    #Crear un objeto de la clase
    mdi = GestorFichas()
    #Mostrar la ventana
    mdi.show()
    #Ejecutar la aplicación
    app.exec_()
    #Estas últias 4 sentencias, lanzan la aplicación. El if evita que se abra en caso de que no sea la principal.