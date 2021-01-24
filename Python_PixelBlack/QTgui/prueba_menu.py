import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, qApp, QStyle, QLabel, QMenu
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from formulario import Formulario1


class Ventana(QMainWindow):
        
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('prueba_menu.ui', self)
        self.define_menu()

    def define_menu(self):
        self.actionClientes.triggered.connect(self.menuClientes)
        self.actionTipo.triggered.connect(self.menuTipo)
        self.actionLogitud.triggered.connect(self.menuLongitud)
        self.actionSangrado.triggered.connect(self.menuSangrado)

    def menuClientes(self):
        sub_ventana = Formulario1()
        self.mdiArea.addSubWindow(sub_ventana)
        self.mdiArea.tileSubWindows()
        sub_ventana.show()

    def menuGuardar(self):
        print('Guardar')

    def menuImprimir(self):
        print('Imprimir')

    def menuTipo(self):
        print('Tipo')

    def menuLongitud(self):
        print('Longitud')

    def menuSangrado(self):
        print('Sangrado')
    
        toggleAction = QAction('Etiqueta con checking', self, checkable=True)
        toggleAction.setStatusTip('Etiqueta con cheking')
        toggleAction.triggered.connect(self.etiqueta_checking)

        exitAction = QAction(QIcon('exit-32.png'), 'Salir', self)  #icono para la accion sacado de un archivo
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Salir de la aplicación')
        exitAction.triggered.connect(qApp.quit)

        menubar = self.menuBar()   #meto el objeto menuBar en una funcion para trabajar con el
        fileMenu = menubar.addMenu('Archivo')  #añado elementos del menu
        fileMenu.addAction(toggleAction)  #añado acciones. Sería los items que cuelgan de cada elemento de menu
        fileMenu.addAction(exitAction)

        # añado submenu
        nuevo_menu = QMenu('nuevo', self)   #creo un objeto de tipo menu. es el que contendrá el submenu
        accion_submenu = QAction('submenu', self)  #creo una accion nueva será la que contendra el submenu      
        nuevo_menu.addAction(accion_submenu)    #añado la accion al submenu     
        fileMenu.addMenu(nuevo_menu)   #añado el submenu al menu padre

    def etiqueta_checking(self, state):
        self.label.setText("El estado del checking es {}".format(state))


app = QApplication(sys.argv)
miVentana = Ventana()
miVentana.show()
app.exec_()