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
                database=self.bd
            )
            self.mycursor = self.mydb.cursor()
        except Exception:
            print("Error al abrir conexion.")
            e = sys.exc_info()
            print(e)

    # insercion en base de datos
    def insertar_tabla(self, vSql):
        try:
            self.mycursor.execute(vSql)
            self.mydb.commit()
        except Exception:
            print("Error al modificar.")
            e = sys.exc_info()
            print(e)

    # modificacion base de datos
    def modificar_tabla(self, vSql):
        try:
            self.mycursor.execute(vSql)
            self.mydb.commit()
        except Exception:
            print("Error al modificar.")
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
    def cerrar(self):
        try:
            self.mycursor.close()
            self.mydb.close()
        except Exception:
            print("Error al cerrar")
            e = sys.exc_info()
            print(e)


if __name__ == "__main__":
    miBD = AccesoBD("localhost", 'estructurados', '12345678aA', 'estructurados')

    vSql = "insert into tabla1 (idtabla1, nombre) values (3, 'jesus3')"
    miBD.conectar()
    miBD.insertar_tabla(vSql)
    miBD.cerrar()

    vSql = "update tabla1 set nombre = 'pepe' where idtabla1 = 2"
    miBD.conectar()
    miBD.modificar_tabla(vSql)
    miBD.cerrar()

    vSql = "select * from tabla1"
    miBD.conectar()
    print(miBD.consulta(vSql))
    miBD.cerrar()