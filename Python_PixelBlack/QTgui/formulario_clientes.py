import sys
from PyQt5 import uic, QtGui, QtCore
from PyQt5.QtWidgets import *

class Form_clientes(QMainWindow):
    dtClientes = {'dni': '', 'nombre': '', 'apellidos': '', 'direccion' : '', 'poblacion': '', 'cp':'', 'provincia': '', 'telefono':'',
        'movil':'', 'email':'', 'web':'', 'fnac':'', 'observaciones': '',  'genero': '', 'deudor':'', 'credito':''}
    
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('formulario_clientes.ui',self)
        self.dtp_fnac.setDate(QtCore.QDate.currentDate())
        self.btn_salir.clicked.connect(self.click_btn_salir)
        self.btn_limpiar.clicked.connect(self.click_btn_limpiar)
        self.btn_aceptar.clicked.connect(self.click_btn_aceptar)

    def click_btn_salir(self):
        #print(self.dtClientes)
        #print(self.cmb_provincia.currentText())
        self.close()
    
    def click_btn_limpiar(self):
        self.txt_dni.clear()
        self.txt_nombre.clear()
        self.txt_apellidos.clear()
        self.txt_direccion.clear()
        self.txt_poblacion.clear()
        self.txt_cp.clear()
        self.txt_telefono.clear()
        self.txt_movil.clear()
        self.txt_email.clear()
        self.txt_web.clear()
        self.txt_observaciones.clear()
        self.chb_deudor.setChecked(False)
        self.chb_credito.setChecked(False)
        self.rdb_hombre.setChecked(True)
        self.cmb_provincia.setCurrentIndex(0) 
        self.dtp_fnac.setDate(QtCore.QDate.currentDate())
        self.txt_dni.setFocus()
    
    def click_btn_aceptar(self):
        #compruebo que se haya escrito un dni
        if self.txt_dni.text() == '':
            QMessageBox.information(self, 'Gestión de Clientes', 'No ha introducido un cliente.')
            self.txt_dni.setFocus()
            return
        
        #codifico el campo genero
        genero = ''
        if self.rdb_hombre.isChecked():
            genero = 'H'
        elif self.rdb_mujer.isChecked():
            genero = 'M'
        else:
            genero = 'O'
        
        #codifico deudor
        deudor = False
        if self.chb_deudor.isChecked():
            deudor = True

        #codifico credito
        credito = False
        if self.chb_credito.isChecked():
            credito = True    

        #compruebo si el cliente existe
        if self.txt_dni.text() in self.dtClientes:
            #modificacion
            print('modificacion')
        else:
            #insercion nueva.
            #  Meto todos los campos en el diccionario
            
            self.dtClientes['dni']=self.txt_dni.text()
            self.dtClientes['nombre']=self.txt_nombre.text()
            self.dtClientes['apellidos']=self.txt_apellidos.text()
            self.dtClientes['direccion']=self.txt_direccion.text()
            self.dtClientes['poblacion']=self.txt_poblacion.text()
            self.dtClientes['cp']=self.txt_cp.text()
            self.dtClientes['telefono']=self.txt_telefono.text()
            self.dtClientes['movil']=self.txt_movil.text()
            self.dtClientes['email']=self.txt_email.text()
            self.dtClientes['web']=self.txt_web.text()
            self.dtClientes['observaciones']=self.txt_observaciones.toPlainText()
            self.dtClientes['genero']=genero
            self.dtClientes['deudor']=deudor
            self.dtClientes['credito']=credito
            self.dtClientes['fnac']=self.dtp_fnac.dateTime().toString('dd-MM-yyyy')
            self.dtClientes['provincia']=self.cmb_provincia.currentText()
            print(self.dtClientes)



           

        #compruebo si el dni existe para saber si es una insercion nueva o una modificacion


if (__name__ == '__main__'):
    app = QApplication(sys.argv)
    miVentana = Form_clientes()
    miVentana.show()
    app.exec_()