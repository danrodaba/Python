import sys
from PyQt5.QtWidgets import *
from accesobd import AccesoBD
from PyQt5 import uic

class FrmClientes(QMainWindow):
    miBD = AccesoBD('localhost', 'estructurados', '12345678aA', 'estructurados')

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('proyecto_bd.ui', self)
        self.dni.setFocus()      #Esto pone el foco en el primer campo del formulario
        self.btn_aceptar.clicked.connect(self.click_btnAceptar)
        self.btn_limpiar.clicked.connect(self.click_btnLimpiar)
        self.btn_cancelar.clicked.connect(self.click_btnCancelar)

    
    def click_btnCancelar(self):
        self.close()  # cierra la ventana (luego añadiremos una ventana de confirmación)
    
    def click_btnLimpiar(self):
        self.dni.clear()
        self.nombre.clear()
        self.direccion.clear()
        self.provincia_2.clear()
        self.fecha_nacimiento.clear
    
    def click_btnAceptar(self):
        self.DNI = self.dni.text()
        self.NOMBRE = self.nombre.text()
        self.DIRECCION = self.direccion.text()
        self.PROVINCIA = self.provincia_2.currentText()
        self.FECHA_NACIMIENTO = self.fecha_nacimiento.dateTime().toString('yyyy-MM-dd')   #con .toString puedo dar formato a la fecha
        self.CREDITO = self.credito.isChecked()


    #Procedemos a la inserción.
        sentencia_SQL = 'insert into cliente (dni, nombre, direccion, provincia, f_nac, credito) values ('
        sentencia_SQL += '"' + self.DNI + '" , "' + self.NOMBRE + '" , "' + self.DIRECCION + '" , "' + self.PROVINCIA + '" , "' + self.FECHA_NACIMIENTO + '" , ' + str(self.CREDITO) + ');'
        print(sentencia_SQL)
        self.miBD.conectar()
        self.miBD.ejecuta_comando_SQL(sentencia_SQL)
        self.miBD.desconectar()

if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    miVentana = FrmClientes()
    miVentana.show()
    app.exec_()