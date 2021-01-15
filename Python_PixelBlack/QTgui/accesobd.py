import mysql.connector
import sys


class AccesoBD:
    servidor = ''
    usuario = ''
    pwd = ''
    bd = ''
    mydb = mysql.connector
    mycursor = None

    # constructor
    def __init__(self, serv, user, pwd, bd):
        self.servidor = serv
        self.usuario = user
        self.pwd = pwd
        self.bd = bd

    # establecemos conexion a la bd
    def conectar(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.servidor,
                user=self.usuario,
                password=self.pwd,
                database=self.bd,
                auth_plugin = 'mysql_native_password'
            )
            self.mycursor = self.mydb.cursor()
        except Exception:
            print("Error al abrir conexion.")
            e = sys.exc_info()
            print(e)

    # insercion en base de datos. Solo inserta un dato en lA BD
    def ejecuta_comando_SQL(self, vSql):
        try:
            self.mycursor.execute(vSql)
            self.mydb.commit()
        except Exception:
            print("Error al insertar.")
            e = sys.exc_info()
            print(e)
            self.mydb.rollback()

    # insercion sin commit. Devuelve cierto si no falla la insercion
    def ejecuta_sin_commit(self, vSql):
        try:
            self.mycursor.execute(vSql)
            return True
        except Exception:
            print("Error al modificar.")
            e = sys.exc_info()
            print(e)
            return False

    # cerrar transaccion
    def cerrar_transaccion(self):
        try:
            self.mydb.commit()
            
        except Exception:
            print("Error al cerrar transacción.")
            e = sys.exc_info()
            print(e)
            
    # realiza un rollback en una transaccion
    def rollback(self):
        try:
            self.mydb.rollback()
            
        except Exception:
            print("Error al hacer rollback.")
            e = sys.exc_info()
            print(e)

    # consulta en bd
    def consulta(self, vSql):
        try:
            self.mycursor.execute(vSql)
            resultado = self.mycursor.fetchall() 
            return resultado
        except Exception:
            print("Error al consultar")
            e = sys.exc_info()
            print(e)
            return None

    # cerrar conexiones
    def desconectar(self):
        try:
            self.mycursor.close()
            self.mydb.close()
        except Exception:
            print("Error al cerrar")
            e = sys.exc_info()
            print(e)


