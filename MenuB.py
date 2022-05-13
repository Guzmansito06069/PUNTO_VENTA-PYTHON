import Reporte
import clientesb


def inicio():
    while True:
        print("\n")
        print("|****************************|")
        print("|**|      Bienvenidos     |**|")
        print("|**|         Menu         |**|")
        print("|**|    Compañia Guzman   |**|")
        print("|****************************|")
        print("")
        print("Seleccione una de las siguientes opciones:");
        print("1.- Clientes")
        print("2.- Articulos")
        print("3.- Reporte")


        opcion = int(input("Opcion: "))

        if opcion == 1:

            clientesb.menuPrincipal()
        elif opcion == 2:
             Reporte.menuPrincipal()
        elif opcion == 3:
            print("FINAL")


if __name__ == '__main__':
    inicio();
