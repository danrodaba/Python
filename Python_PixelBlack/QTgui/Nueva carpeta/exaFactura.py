import sys
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from formulario import Formulario

#Clase heredada de QMainWindow (Constructor de Ventanas)
class ExaFactura(QMainWindow): 
   
    def __init__(self):
        super().__init__()
        uic.loadUi('exaFactura.ui',self)
        #Añadir Titulo
        self.setWindowTitle('ExaFactura') 
        #Añadir icono
        self.setWindowIcon(QIcon('factura.png'))
        self.menu()

    #Añadimos las acciones para la barra menu
    def menu(self):
        self.actionClientes.triggered.connect(self.abrirClientes)
        self.actionSalir.triggered.connect(self.cerrar)

    #Función que al pulsar el boton de clientes, abre el formulario
    def abrirClientes(self):
        subVentana=Formulario()
        self.mdiArea.addSubWindow(subVentana) 
        subVentana.show()
        self.mdiArea.tileSubWindows()        
    
    #Función que al pulsar el boton de cerrar, abre un cuadro de dialogo que pregunta si cerramos o no
    def cerrar(self):
        mensaje=QMessageBox.question(self, 'Formulario Clientes','¿Desea Salir?')      
        if mensaje==QMessageBox.Yes:self.close()
        
        

app=QApplication(sys.argv)
mdi=ExaFactura()
mdi.show()
app.exec_()                