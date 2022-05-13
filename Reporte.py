from BD.conexiond import DAO
import funcionesd


def menuPrincipal():
     while True:
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar Reportes")
            print("2.- Registrar Reportes")
            print("3.- Actualizar Reportes")
            print("4.- Eliminar Reportes")
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
                funcionesd.listarCC(cc)
            else:
                print("No se encontraron Reportes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 2:
        reporte1 = funcionesd.pedirDatosRegistro()
        try:
            dao.registrarC(reporte1)
        except:
            print("Ocurrió un error...")
    elif opcion == 3:
        try:
            cc = dao.listaC()
            if len(cc) > 0:
                reporte1 = funcionesd.pedirDatosActualizacion(cc)
                if reporte1:
                    dao.actualizarC(reporte1)
                else:
                    print("Id del Reporte a actualizar no encontrado...\n")
            else:
                print("No se encontraron Reportes...")
        except:
            print("Ocurrió un error...")
    elif opcion == 4:
        try:
            cc = dao.listaC()
            if len(cc) > 0:
                codigoEliminar = funcionesd.pedirDatosEliminacion(cc)
                if not(codigoEliminar == ""):
                    dao.eliminarC(codigoEliminar)
                else:
                    print("Id del Reporte no se ha encontrado...\n")
            else:
                print("No se encontraron Reportes...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")

if __name__ == '__main__':
   menuPrincipal()