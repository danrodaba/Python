import sys
from PyQt5 import uic
from PyQt5.QtWidgets import *
from accesobd import AccesoBD

class Formulario1(QMainWindow):

    miBD = AccesoBD('localhost', 'estructurados', '12345678aA', 'estructurados')

    datos = []

    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('formulario.ui', self)
        self.btn_aceptar.clicked.connect(self.click_aceptar)
        self.btn_salir.clicked.connect(self.click_btnCancelar)
        self.btn_limpiar.clicked.connect(self.click_btnLimpiar)
        self.btn_eliminar.clicked.connect(self.click_btnEliminar)


    def click_btnEliminar(self):
        sentencia_SQL = 'delete from cliente where DNI = "' + self.DNI_NIE.text() + '";'
        if self.DNI_NIE.text() == '':
            sentencia_SQL = 'delete from cliente where DNI = null'
        self.miBD.conectar()
        self.miBD.ejecuta_comando_SQL(sentencia_SQL)
        self.miBD.desconectar()

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
        self.CCAA_cbb.clear()
        self.email.clear()
        self.cbx_deudor.setChecked(False)
        self.cbx_credito.setChecked(False)
        self.observaciones.clear()
        self.rdbtn_hombre.setChecked(True)
        self.nacimiento.clear()

        
    def click_aceptar(self):        # Al aceptar se imprimirán los resultados como una lista
        self.datos.append(self.DNI_NIE.text())
        self.datos.append(self.nombre.text())
        self.datos.append(self.apellidos.text())
        self.datos.append(self.direccion.text())
        self.datos.append(self.CCAA_cbb.currentText())
        self.datos.append(self.provincia.text())
        self.datos.append(self.poblacion.text())
        self.datos.append(self.cp.text())
        self.datos.append(self.telefono.text())
        self.datos.append(self.email.text())
        if self.rdbtn_hombre.isChecked():
            self.datos.append('hombre')
        elif self.rdbtn_muje.isChecked():
            self.datos.append('mujer')
        elif self.rdbtn_NoBinario.isChecked():
            self.datos.append('no binario')
        else:
            self.datos.append('hombre')
        self.datos.append(self.nacimiento.dateTime().toString('yyyy-MM-dd'))
        self.datos.append(self.observaciones.toPlainText())
        self.datos.append(self.cbx_deudor.isChecked())
        self.datos.append(self.cbx_credito.isChecked())
        for i in range(len(self.datos)):
            if self.datos[i] == '':
                self.datos[i] = 'null'

        #ahora procedo a meterlo en la base de datos
        sentencia_SQL = 'insert into cliente (dni, nombre, apellidos, direccion, comunidad_autonoma, provincia, poblacion, cp, telefono, email, sexo, fnac, observaciones, deudor, credito) values ('
        sentencia_SQL += '"' + str(self.datos[0])
        for i in self.datos[1:-2]:
            sentencia_SQL +=  '" , "' + str(i)
        sentencia_SQL += '"'
        for i in self.datos[-2:len(self.datos)]:
            sentencia_SQL +=  ', ' + str(i)
        sentencia_SQL += ')'
        sentencia_SQL=sentencia_SQL.replace('"null"', 'null')
        if len(self.datos[0]) == 9:
            self.miBD.conectar()
            self.miBD.ejecuta_comando_SQL(sentencia_SQL)
            self.miBD.desconectar()
        else:
            print('No has introducido un DNI válido (8 cifras + 1 letra).')

        self.datos = []


if __name__ == '__main__':
    app = QApplication(sys.argv)
    miVentana = Formulario1()
    miVentana.show()
    app.exec_()