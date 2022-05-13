
#Importo Librerias
import os.path
import json
#Creo clase Clientes
class clientes:
#Creo Lista regC
    regC = []

    def __init__(self, id, nombre, rfc, direccion):
        self.id = id
        self.nombre = nombre
        self.rfc = rfc
        self.direccion = direccion
        self.__idx__ = 0

    def __init__(self):
        self.id = ''
        self.nombre = ''
        self.rfc = ''
        self.direccion = ''
        self.__idx__ = 0

    def __init__(self, regC=list()):
        self.regC = regC

    def __str__(self):
        datos = "ID: " + self.id + " // Nombre: " + self.nombre + " // RFC: " + self.rfc + " // Direccion: " + self.direccion
        return datos

    def agregarCliente(self, cl):
        self.regC.append(cl)

    def imprimirClientes(self):
        a = self.regC
        return a

    def buscarCliente(self, x=int()):
        try:
            b = self.regC[x - 1]
            return b
        except Exception as e:
            return "No se encontro el elemento"

    def eliminarCliente(self, ide=int()):
        try:
            c = self.regC.pop(ide - 1)
            return c
        except Exception as e:
            return "No se encontro el elemento a eliminar"
    
    def modificarCliente(self, rem, index=int()):
        try:
            d = self.regC[index - 1] = rem
            return d
        except Exception as e:
            return "No se encontro el elemento a modificar"

    def convDicC(self):
        return {
            "ID": self.id,
            "Nombre": self.nombre,
            "RFC": self.rfc,
            "Direccion": self.direccion
        }

    def lisDicC(self):
        lis = list()
        for i in self.regC:
            lis.append(i.convDicC())
        return lis

    def toJsonC(self, lisdic):
        try:
            file = open("clientes.json", "w")
            file = json.dump(lisdic, file)
            return "Archivo creado y datos guardados"
        except:
            return "No se creo ni se guardo nada en el archivo"

    def obtenerJSonC(self):
        data = []
        if os.path.isfile("clientes.json"):
            file = open("clientes.json", "r")
            data = json.loads(file.read())
        return data

    def cargarObjC(self):
        data = self.obtenerJSonC()
        for x in data:
            c = clientes()
            c.id = x["ID"]
            c.nombre = x["Nombre"]
            c.rfc = x["RFC"]
            c.direccion = x["Direccion"]
            self.regC.append(c)