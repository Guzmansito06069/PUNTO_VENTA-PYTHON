import mysql.connector
from mysql.connector import Error


class DAO():

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(host='localhost', user='root', password='', database='pythonsistema')
        except Error as ex:
            print("Error al intentar la conexión: {0}".format(ex))

    def listaC(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute("SELECT * FROM clientes ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarC(self, clientes):
        print('clientes', clientes)
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO clientes (id, nombre, rfc,direccion) VALUES ( '{0}', '{1}' , '{2}', '{3}')"
                cursor.execute(sql.format(clientes[0], clientes[1], clientes[2],clientes[3]))
                self.conexion.commit()
                print("¡Cliente registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarC(self, clientes):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE clientes SET nombre = '{0}', rfc = '{1}' ,direccion = '{3}' WHERE id = '{2}'"
                cursor.execute(sql.format(clientes[1], clientes[2],clientes[3], clientes[0]))
                self.conexion.commit()
                print("¡Cliente actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarC(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM clientes WHERE id = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Clientes eliminado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))