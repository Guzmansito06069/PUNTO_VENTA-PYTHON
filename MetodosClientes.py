import clientes
import articulos
import ventas

dataC = clientes.clientes()
dataA = articulos.articulos()
dataV = ventas.ventas()
dataA.obtenerJSonA()
dataC.obtenerJSonC()
dataC.cargarObjC()
dataA.cargarObjA()


def ingresaCl():
  print("|****************************|")
  print("|***********-INGRESAR CLIENTE-*********|")
  print("|****************************|")
  cant = int(input("¿Cuantos clientes desea ingresar? (Ingrese 0 para salir): "))
  print(" ")

  for lim in range(0, cant):
    ide = input("ID: ")
    nom = input("Nombre: ")
    rfc = input("RFC: ")
    dire = input("Direccion: ")

    cl = clientes.clientes()
    ag = clientes.clientes()

    cl.id = ide
    cl.nombre = nom
    cl.rfc = rfc
    cl.direccion = dire
    ag.agregarCliente(cl)
    print("\n")

print("\nClientes agregados")

def mostrar():
  print("|****************************|")
  print("|***********-MOSTRAR CLIENTE-*********|")
  print("|****************************|")
  li = clientes.clientes()
  if li.regC == []:
    print("\nLista vacia")
  else:
    for l in li.imprimirClientes():
      print(l)

def eliminar():
  print("|****************************|")
  print("|***********-ELIMINAR CLIENTE-*********|")
  print("|****************************|")
  elim = clientes.clientes()
  if elim.regC == []:
    print("List vacia")
  else:
    for i in elim.imprimirClientes():
      print(i)

    dele = int(input("\nIngrese el id a eliminar: "))
    print("\nEl cliente eliminado fue: \n")
    print(elim.eliminarCliente(dele))