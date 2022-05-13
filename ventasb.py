from BD.conexionv import DAO
import funcionesv


def menuPrincipal():
     while True:
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Mostrar Ventas")
            print("2.- Agregar Ventas")
            print("3.- Modificar Ventas")
            print("4.- Eliminar Ventas")
            print("5.- Salir")
            print("========================================================")
            opcion = int(input("Seleccione una opción: "))

            if opcion < 1 or opcion > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif opcion == 5:
                continuar = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                opcionCorrecta = True
                ejecutarOpcion(opcion)

def ejecutarOpcion(opcion):
    dao = DAO()

    if opcion == 1:
        try:
            cc = dao.listaC()
            if len(cc) > 0:
                funcionesv.listarCC(cc)
            else:
                print("No se encontraron articulos...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        clientes = funcionesv.pedirDatosRegistro()
        try:
            dao.registrarC(clientes)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            cc = dao.listaC()
            if len(cc) > 0:
                clientes = funcionesv.pedirDatosActualizacion(cc)
                if clientes:
                    dao.actualizarC(clientes)
                else:
                    print("Id de la venta a actualizar no encontrado...\n")
            else:
                print("No se encontraron clientes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            cc = dao.listaC()
            if len(cc) > 0:
                codigoEliminar = funcionesv.pedirDatosEliminacion(cc)
                if not(codigoEliminar == ""):
                    dao.eliminarC(codigoEliminar)
                else:
                    print("Código de venta no encontrado...\n")
            else:
                print("No se encontraron clientes...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

if __name__ == '__main__':
   menuPrincipal()