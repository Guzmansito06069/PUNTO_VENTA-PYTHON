import MENUBD
import clientesb
import main

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
        print("1.- BASE DE DATOS")
        print("2.- JSON")
        print("3.- Salir")


        opcion = int(input("Opcion: "))

        if opcion == 1:

            MENUBD.inicio2()
        elif opcion == 2:
            main.iniciojson()
        elif opcion == 3:
            print("FINAL")


if __name__ == '__main__':
    inicio();
