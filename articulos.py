import os.path
import json
class articulos:

    regA = []

    def __init__(self, id, clave, nom):
        self.id = id
        self.clave = clave
        self.nom = nom

    def __init__(self):
        self.id = ''
        self.clave = ''
        self.nom = ''

    def __init__(self, regA=list()):
        self.regA = regA

    def agregarArticulo(self, ar):
        self.regA.append(ar)

    def imprimirArticulos(self):
        a = self.regA
        return a

    def __str__(self):
        datos = "ID: " + self.id + " // Clave: " + self.clave + " // Nombre: " + self.nom
        return datos

    def buscarArticulo(self, x=int()):
        try:
            b = self.regA[x - 1]
            return b
        except Exception as e:
            return "No se encontro el elemento"

    def eliminarArticulo(self, ide=int()):
        try:
            c = self.regA.pop(ide - 1)
            return c
        except Exception as e:
            return "No se encontro el elemento a eliminar"

    def modificarArticulo(self, rem, index=int()):
        try:
            d = self.regA[index - 1] = rem
            return d
        except Exception as e:
            return "No se encontro el elemento a modificar"

    def convDicA(self):
        return {
            "ID": self.id,
            "Clave":self.clave,
            "Nombre":self.nom
        }

    def lisDicA(self):
        lis = list()
        for i in self.regA:
            lis.append(i.convDicA())
        return lis

    def toJsonA(self, lisdic):
        try:
            file = open("articulos.json", "w")
            file = json.dump(lisdic, file)
            return "Archivo creado y datos guardados"
        except:
            return "No se creo ni se guardo nada en el archivo"

    def obtenerJSonA(self):
        data = []
        if os.path.isfile("articulos.json"):
            file = open("articulos.json", "r")
            data = json.loads(file.read())
        return data

    def cargarObjA(self):
        data = self.obtenerJSonA()
        for x in data:
            a = articulos()
            a.id = x["ID"]
            a.clave = x["Clave"]
            a.nom = x["Nombre"]
            self.regA.append(a)