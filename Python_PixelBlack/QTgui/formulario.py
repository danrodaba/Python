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

        vSql = "DELETE FROM cliente  "
        vSql = vSql + "WHERE dni = '" + self.DNI_NIE.text() + "'"
        
        self.miBD.conectar()
        self.miBD.ejecuta_comando_SQL(vSql)
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
        self.email.clear()
        self.cbx_deudor.setChecked(False)
        self.cbx_credito.setChecked(False)
        self.observaciones.clear()
        self.rdbtn_hombre.setChecked(True)
        self.nacimiento.clear()

        
    def click_aceptar(self):        # Al aceptar se imprimirán los resultados como una lista
        
        # primero vamos a crear una sentencia para saber si creamos o modificamos una entrada de la base de datos.
        self.DNI = str(self.DNI_NIE.text())
        self.SQL_busqueda = "select * from cliente where DNI = '" + self.DNI + "'"
        self.miBD.conectar()
        self.respuesta_SQL = self.miBD.consulta(self.SQL_busqueda)
        self.miBD.desconectar()
        #ahora rellenamos con los datos nuestra lista "datos"
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

        self.campos = 'dni nombre apellidos direccion comunidad_autonoma provincia poblacion cp telefono email sexo fnac observaciones deudor credito'.split()
        
        if self.respuesta_SQL == []: # si la respuesta está vacía, no existe la entrada y se crea nueva:

            #ahora procedo a meterlo en la base de datos

            self.sentencia_SQL = 'insert into cliente (dni, nombre, apellidos, direccion, comunidad_autonoma, provincia, poblacion, cp, telefono, email, sexo, fnac, observaciones, deudor, credito) values ('
            self.sentencia_SQL += '"' + str(self.datos[0])
            for i in self.datos[1:-2]:
                self.sentencia_SQL +=  '" , "' + str(i)
            self.sentencia_SQL += '"'
            for i in self.datos[-2:len(self.datos)]:
                self.sentencia_SQL += ', ' + str(i)
            self.sentencia_SQL += ')'
            self.sentencia_SQL = self.sentencia_SQL.replace('"null"', 'null')       #esto quita las comillas a los 'null'
            if len(self.datos[0]) == 9:
                self.miBD.conectar()            # aquí tienes la conexión
                self.miBD.ejecuta_comando_SQL(self.sentencia_SQL)
                self.miBD.desconectar()         # aquí la desconexión
            else:
                print('No has introducido un DNI válido (8 cifras + 1 letra).')

            self.datos = []
        else:       # si la entrada no está vacía, el campo existe y solamente se va a actualizar.
            self.actualizar = 'UPDATE cliente SET '
            for i in range(len(self.datos)-1):
                self.actualizar += str(self.campos[i+1]) + ' = '
                self.actualizar += ' "' + str(self.datos[i+1]) + '", '
            self.actualizar = self.actualizar[0:-2] + ' WHERE DNI = "' + str(self.DNI) + '";'
            self.actualizar = self.actualizar.replace('"null"', 'null')
            self.actualizar = self.actualizar.replace('"False"', 'False')
            self.actualizar = self.actualizar.replace('"True"', 'True')
            self.miBD.conectar()
            self.miBD.ejecuta_comando_SQL(self.actualizar)
            self.miBD.desconectar()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    miVentana = Formulario1()
    miVentana.show()
    app.exec_()