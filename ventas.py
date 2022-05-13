from articulos import articulos
from clientes import clientes
import json
import os.path


class ventas(clientes, articulos):
    lista=[]

    def __init__(self):
        self.id_v = ''
        self.fecha_v = ''
        self.pre_a = 0.0
        self.cant_a = 0
        self.sub_v = 0.0
        self.iva_v = 0.0
        self.total_v = 0.0
        '''
        self.lista = list()
        '''
    def agregarVenta(self, lis):
        print(lis)

        self.lista.append(lis)
        print(self.lista)
    def mostrarVentas(self):
        mos = self.lista
        return mos

    def __str__(self):
        ventaa = "ID: " + self.id_v + "\nFecha: " + self.fecha_v + "\nCliente: " + str(self.Cliente) + "\nArticulo: " + str(self.Articulo) + "\nCantidad de articulos: " + str(self.cant_a) + "\nPrecio del articulo: $" + str(self.pre_a) + "\nTotal de ventas: $" + str(self.total_v)
        return ventaa

    def buscarVenta(self, x=int()):
        try:
            bu = self.lista[x - 1]
            return bu
        except Exception as e:
            return "La lista esta vacia, no hay nada que buscar"

    def __iva__(self):
        self.iva_v = self.pre_a * 0.16 * self.cant_a

    def __subt__(self):
        self.sub_v = self.pre_a * self.cant_a

    def __total__(self):
        self.total_v = self.sub_v + self.iva_v

    def calculo(self):
        self.__iva__()
        self.__subt__()
        self.__total__()

    def convDicV(self):
        return {
            "ID_v": self.id,
            "Fecha": self.fecha_v,
            "Cliente": str(self.Cliente),
            "Articulo": str(self.Articulo),
            "Precio": str(self.pre_a),
            "Cantidad": str(self.cant_a),
            "Total": str(self.total_v)
        }

    def lisDicV(self):
        lis = list()
        for i in self.lista:
            lis.append(i.convDicA())
            print(list)
        return lis

    def JsonV(self, lisdicv):
        file = open("ventas.json", "w")
        file = json.dump(lisdicv, file)

    def obtenerJSonV(self):
        data = []
        if os.path.isfile("ventas.json"):
            file = open("ventas.json", "r")
            data = json.loads(file.read())
        return data

    def cargarObjV(self):
        data = self.obtenerJSonA()
        for x in data:
            v = ventas()
            v.id_v = x["ID_v"]
            v.fecha_v = x["Fecha"]
            v.Cliente = x["Cliente"]
            v.Articulo = x["Articulo"]
            v.pre_a = x["Precio"]
            v.cant_a = x["Cantidad"]
            v.total_v = x["Total"]
            self.lista.append(v)

if __name__ == '__main__':
    while True:
        print("MENU\n1.-Cliente\n2.-Articulo\n3.-Venta")
        op = int(input("Ingrese la opcion: "))
        if op == 1:
            print("MENU Cliente\n1.-Insertar\n2.-Mostrar\n3.-Salir")
            opc = int(input("Ingrese la opcion: "))
            if opc == 1:
                cant = int(input("Ingrese la cantidad de datos: "))
                for lim in range(0, cant):
                    ide = input("ID: ")
                    nom = input("Nombre: ")
                    rfc = input("RFC: ")
                    dire = input("Direccion: ")

                    cl = clientes()
                    ag = clientes()

                    cl.id = ide
                    cl.nombre = nom
                    cl.rfc = rfc
                    cl.direccion = dire
                    ag.agregarCliente(cl)
                    print("\n")

                print("\nClientes agregados")
            elif opc == 2:
                li = clientes()
                if li.regC == []:
                    print("\nLista vacia")
                else:
                    for l in li.imprimirClientes():
                        print(l)
            elif opc == 3:
                break
        elif op == 2:
            print("\nMENU Articulo\n1.-Insertar\n2.-Mostrar\n3.-Salir")
            opa = int(input("Ingrese la opcion: "))
            if opa == 1:
                can = int(input("Ingrese la cantidad de datos: "))
                print("\n")
                for lim in range(0, can):
                    id_a = input("ID: ")
                    cve_a = input("Clave: ")
                    nom_a = input("Nombre: ")
                    ar = articulos()
                    ag = articulos()
                    ar.id = id_a
                    ar.clave = cve_a
                    ar.nom = nom_a
                    ag.agregarArticulo(ar)
                    print("\n")
            elif opa == 2:
                mos = articulos()
                if mos.regA == []:
                    print("\nLista vacia")
                else:
                    for m in mos.imprimirArticulos():
                        print(m)
            elif opa == 3:
                break

                '''---------------------------------------------------------------------------------------------'''
        elif op == 3:
            print("\nMENU Ventas\n1.-Ingresar\n2.-Mostrar\n3.-Guardar\n4.-Salir")
            opv = int(input("Ingrese la opcion: "))
            if opv == 1:
                cl = clientes()
                ar = articulos()
                if cl.regC == [] or ar.regA == []:
                    print("No se han ingresado datos en ningun lado")
                else:
                    print("Clientes disponibles")
                    for cli in cl.imprimirClientes():
                        print(cli)
                    print("\n")
                    print("Articulos disponibles")
                    for art in ar.imprimirArticulos():
                        print(art)
                    print("\n")

                    ide_v = input("ID de la venta: ")
                    ide_c = int(input("\nID del cliente: "))
                    cant = int(input("¿Cuantos articulos desea ingresar?"))
                    print("\n")

                    ide_a = int(input("\nID del articulo: "))
                    fecha = input("\nFecha: ")
                    cantidad = int(input("\nCantidad de articulos: "))
                    prec = float(input("\nPrecio del articulo: "))

                    if cl.buscarCliente(ide_c) == "No se encontro el elemento":
                        print(cl.buscarCliente(ide_c))
                    elif ar.buscarArticulo(ide_a) == "No se encontro el elemento":
                        print(ar.buscarArticulo(ide_a))
                    else:
                        v = ventas()
                        ve = ventas()
                        v.id_v = ide_v
                        v.Cliente = cl.buscarCliente(ide_c)
                        v.Articulo = ar.buscarArticulo(ide_a)
                        v.fecha_v = fecha
                        v.cant_a = cantidad
                        v.pre_a = prec
                        v.calculo()
                        myVenta = ventas()
                        myVenta.agregarVenta(v)
            elif opv == 2:
                mosV = ventas()
                if mosV.lista == []:
                    print("La lista esta vacia")
                else:
                    for mex in mosV.mostrarVentas():
                        print(mex)
            elif opv == 3:
                ven = ventas()
                if ven.lista == []:
                    print("Lista esta vacia, no hay registros por guardar")
                else:
                    conVen = ven.lisDicV()
                    ven.JsonV(conVen)
            elif opv == 4:
                break
        else:
            break