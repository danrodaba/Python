import sys
from PyQt5 import uic, QtGui
#from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMessageBox, qApp, QStyle, QLabel, QMenu, QMdiArea, QMdiSubWindow, QTextEdit
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from formulario_clientes import Form_clientes

class MdiArea3(QMainWindow):
        
    def __init__(self):
        super().__init__()
        uic.loadUi('mdiarea3.ui',self)
        self.define_menu()
        

    def define_menu(self):
        self.act_abrir.triggered.connect(self.accion_abrir)

    def accion_abrir(self):
        sub_ventana = Form_clientes()
        self.mdiArea.addSubWindow(sub_ventana)
        self.mdiArea.tileSubWindows()
        sub_ventana.show()

app = QApplication(sys.argv)
mdi  =MdiArea3()
mdi.show()
app.exec_()