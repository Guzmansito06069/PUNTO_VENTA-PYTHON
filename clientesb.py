from BD.conexion import DAO
import funciones


def menuPrincipal():
     while True:
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar clientes")
            print("2.- Registrar clientes")
            print("3.- Actualizar clientes")
            print("4.- Eliminar clientes")
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
                funciones.listarCC(cc)
            else:
                print("No se encontraron clientes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        clientes = funciones.pedirDatosRegistro()
        try:
            dao.registrarC(clientes)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            cc = dao.listaC()
            if len(cc) > 0:
                clientes = funciones.pedirDatosActualizacion(cc)
                if clientes:
                    dao.actualizarC(clientes)
                else:
                    print("Id del cliente a actualizar no encontrado...\n")
            else:
                print("No se encontraron clientes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            cc = dao.listaC()
            if len(cc) > 0:
                codigoEliminar = funciones.pedirDatosEliminacion(cc)
                if not(codigoEliminar == ""):
                    dao.eliminarC(codigoEliminar)
                else:
                    print("Id del cliente no encontrado...\n")
            else:
                print("No se encontraron clientes...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

if __name__ == '__main__':
   menuPrincipal()

