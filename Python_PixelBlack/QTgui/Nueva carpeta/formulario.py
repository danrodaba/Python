import sys
from PyQt5 import uic, QtCore
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *
from connDB import ConnDB

#Clase heredada de QMainWindow (Constructor de Ventanas)
class Formulario(QMainWindow): 
    #Accedemos a la base de datos
    conn = ConnDB("localhost", 'estructurados', '12345678aA', 'estructurados') 
    #Método constructor de la clase
    def __init__(self):        
        #Iniciar el objeto QMainWindow
        QMainWindow.__init__(self)
        #Cargar la configuración del archivo .ui en el objeto
        uic.loadUi("formulario.ui",self)  
        #Añadir Titulo
        self.setWindowTitle('Formulario Clientes') 
        #Añadir icono
        self.setWindowIcon(QIcon('lapiz.png'))
        #Ponemos el foco en el primer campo del formulario  
        self.txtDni.setFocus()    
      
        #Llamamos a las funciones cuando pulsemos los botones correspondientes       
        self.btnLimpiar.clicked.connect(self.limpiar) 
        self.btnAceptar.clicked.connect(self.addDb) 
        self.btnEliminar.clicked.connect(self.eliminarDb) 
        self.btnImprimir.clicked.connect(self.mostrarDb)   
        self.btnSalir.clicked.connect(self.cerrarVentanaClientes)

    #Función que al pulsar el boton guardar introduce datos en la base de datos
    def addDb(self):       
        if self.txtDni.text() == '':
            QMessageBox.information(self, 'exaFactura:Formulario Clientes', 'El DNI del cliente no puede estar vacío.')
            self.txtDni.setFocus()
            return
        
        # compruebo si es una insercion nueva o una modificacion
        insercion = False
        vSql = "SELECT * FROM clientes WHERE dni = '" + self.txtDni.text() + "'"
        self.conn.conectar()
        resultado = self.conn.consulta(vSql)
        self.conn.desconectar()
        if len(resultado) == 0:
            insercion = True   # es una insercion de un cliente nuevo
        
        if insercion:
            # insercion nueva
            vSql = "INSERT INTO clientes (dni, nombre, direccion,provincia,poblacion,cp,telefono,email,observaciones) values ("
            vSql = vSql + "'" + self.txtDni.text() + "', "
            vSql = vSql + "'" + self.txtNombre.text() + "', "
            vSql = vSql + "'" + self.txtDirec.text() + "', "
            vSql = vSql + "'" + self.cbProvincia.currentText()+"', "
            vSql = vSql + "'" + self.txtPobla.text() + "', "
            vSql = vSql + "'" + self.txtCp.text() + "', "
            vSql = vSql + "'" + self.txtTlf.text() + "', "
            vSql = vSql + "'" + self.txtMail.text() + "', "
            vSql = vSql + "'" + self.txtObser.toPlainText() + "')"
            
            self.conn.conectar()
            self.conn.ejecuta_comando_SQL(vSql)
            self.conn.desconectar()

            QMessageBox.information(self, 'ExaFactura: Formulario de Clientes', 'Cliente introducido correctamente.')
            self.limpiar()
           
        else:
            # modificacion de un cliente existente
            vSql = "UPDATE clientes SET "
            vSql = vSql + "nombre = '" + self.txtNombre.text() + "', "
            vSql = vSql + "direccion = '" + self.txtDirec.text() + "', "
            vSql = vSql + "provincia = '" + self.cbProvincia.currentText() + "', "
            vSql = vSql + "poblacion = '" + self.txtPobla.text()+ "', "
            vSql = vSql + "cp = '" + self.txtCp.text() + "', "
            vSql = vSql + "telefono = '" + self.txtTlf.text() + "', "
            vSql = vSql + "email = '" + self.txtMail.text() + "', "
            vSql = vSql + "observaciones = '" + self.txtObser.toPlainText() + "' "            
            vSql = vSql + "WHERE dni = '" + self.txtDni.text() + "'"
            self.conn.conectar()
            self.conn.ejecuta_comando_SQL(vSql)
            self.conn.desconectar()

            QMessageBox.information(self, 'ExaFactura', 'Cliente modificado correctamente.')
            self.limpiar()

    #Función que al pulsar el boton borrar, elimina los datos en la base de datos
    def eliminarDb(self):
        # eliminacion de un cliente existente
            vSql = "DELETE FROM clientes  "                   
            vSql = vSql + "WHERE dni = '" + self.txtDni.text() + "'"
            self.conn.conectar()
            self.conn.ejecuta_comando_SQL(vSql)
            self.conn.desconectar()
            
            QMessageBox.information(self, 'ExaFactura', 'Cliente eliminado correctamente.')
            self.limpiar()

    #Función que muestra por pantalla los datos de la base de datos    
    def mostrarDb(self):
        QMessageBox.information(self, 'ExaFactura', 'Funcionalidad en mantenimiento. Perdone las molestias.')

    #Función que al ser llamada limpia el formulario
    def limpiar(self):
        self.txtDni.setText('')
        self.txtNombre.setText('') 
        self.txtDirec.setText('') 
        self.txtPobla.setText('') 
        self.txtCp.setText('') 
        self.txtTlf.setText('')         
        self.txtMail.setText('')       
        self.txtObser.setText('') 
        self.cbProvincia.setCurrentIndex(0)        
        self.txtDni.setFocus() 

    #Función que cierra la ventana de clientes
    def cerrarVentanaClientes(self):     
        # cierra la ventana       
        self.close()

if __name__=="__main__":
    #Instancia para iniciar una aplicación    
    app = QApplication(sys.argv)
    #Crear un objeto de la clase
    formulario=Formulario()  
    #Mostrar la ventana
    formulario.show()
    #Ejecutar la aplicación
    sys.exit(app.exec_())
    