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
                cursor.execute("SELECT * FROM reporte1 ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def registrarC(self, reporte1):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO reporte1 (id,dia, iva, subtotal,total) VALUES ( '{0}', '{1}' , '{2}', '{3}', '{4}','{5}')"
                cursor.execute(sql.format(reporte1[0], reporte1[1], reporte1[2],reporte1[3],reporte1[4]))
                self.conexion.commit()
                print("¡Reporte registrado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def actualizarC(self, reporte1):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "UPDATE reporte SET  dia = '{0}', iva = '{1}' ,subtotal = '{3}',total='{4}' WHERE id = '{2}'"
                cursor.execute(sql.format(reporte1[1], reporte1[2],reporte1[3], reporte1[4] ,reporte1[0]))
                self.conexion.commit()
                print("¡Reporte actualizado!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))

    def eliminarC(self, codigoCursoEliminar):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "DELETE FROM reporte1 WHERE id = '{0}'"
                cursor.execute(sql.format(codigoCursoEliminar))
                self.conexion.commit()
                print("¡Venta eliminada!\n")
            except Error as ex:
                print("Error al intentar la conexión: {0}".format(ex))