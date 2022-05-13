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
                cursor.execute("SELECT * FROM venta ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarC(self, venta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO venta (id, idc, ida,fecha,precio,total) VALUES ( '{0}', '{1}' , '{2}', '{3}', '{4}', '{5}')"
                cursor.execute(sql.format(venta[0], venta[1], venta[2],venta[3], venta[4],venta[5]))
                self.conexion.commit()
                print("¡Venta registrada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarC(self, venta):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE venta SET idc = '{0}', ida = '{1}' ,fecha = '{3}',precio='{4}',total='{5} WHERE id = '{2}'"
                cursor.execute(sql.format(venta[1], venta[2],venta[3], venta[4],venta[5], venta[0]))
                self.conexion.commit()
                print("¡Venta actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarC(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM venta WHERE id = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Venta eliminada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))