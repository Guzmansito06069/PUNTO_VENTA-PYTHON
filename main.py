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

def iniciojson():
 while True:
    print("|****************************|")
    print("|**|      Bienvenidos     |**|")
    print("|**|         Menu         |**|")
    print("|**|    Compañia Guzman   |**|")
    print("|****************************|")
    print("")
    print("Seleccione una opcion:");
    print("|****************************|")
    print("1.- Clientes")
    print("|****************************|")
    print("2.- Articulos")
    print("|****************************|")
    print("3.- Ventas")
    print("|****************************|")
    print("4.- Salir\n")
    print("|****************************|")
    try:
        op1 = int(input("Ingrese la opcion que desea ver: "))

        if op1 == 1:

            while True:
                print("|****************************|")
                print("|**|      Bienvenidos     |**|")
                print("|**|         Menu         |**|")
                print("|**|    Compañia Guzman   |**|")
                print("|****************************|")
                print("|***********-Cliente-*********|")
                print("|****************************|")
                print("1.- Ingresar clientes\n")
                print("2.- Mostrar clientes\n")
                print("3.- Eliminar clientes\n")
                print("4.- Buscar clientes\n")
                print("5.- Modificar clientes\n")
                print("6.- Guardar clientes\n")
                print("7.- Regresar\n")
                print("|****************************|")
                try:

                    op2 = int(input("Ingrese el numero que desea ejecutar: "))

                    if op2 == 1:

                        print("|****************************|")
                        print("|***********-INGRESAR CLIENTE-*********|")
                        print("|****************************|")
                        cant = int(input("¿Cuantos clientes desea ingresar?"))
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

                        print("\nClientes agregados")

                    elif op2 == 2:

                        print("|****************************|")
                        print("|***********-MOSTRAR CLIENTE-*********|")
                        print("|****************************|")
                        li = clientes.clientes()
                        if li.regC == []:
                            print("\nLista vacia")
                        else:
                            for l in li.imprimirClientes():
                                print(l)

                    elif op2 == 3:

                        print("|****************************|")
                        print("|***********-ELIMINAR CLIENTE-*********|")
                        print("|****************************|")
                        elim = clientes.clientes()
                        if elim.regC == []:
                            print("List vacia")
                        else:
                            for i in elim.imprimirClientes():
                                print(i)

                            dele = int(input("\nIngrese la posicion a eliminar: "))
                            print("\nEl cliente eliminado fue: \n")
                            print(elim.eliminarCliente(dele))

                    elif op2 == 4:

                        print("|****************************|")
                        print("|***********-BUSCAR CLIENTE-*********|")
                        print("|****************************|")
                        bus = clientes.clientes()
                        if bus.regC == []:
                            print("Lista vacia")
                        else:
                            b = int(input("Ingrese el ID del cliente que desea buscar: "))
                            print("\nEl usuario que buscabas es: \n")
                            print(bus.buscarCliente(b))

                    elif op2 == 5:

                        print("|****************************|")
                        print("|***********-MODIFICAR CLIENTE-*********|")
                        print("|****************************|")
                        ver = clientes.clientes()
                        if ver.regC == []:
                            print("Lista vacia")
                        else:
                            for i in ver.imprimirClientes():
                                print(i)

                            r = int(input("\nIngrese el ID del cliente que desea modificar: "))
                            print("\nEl usuario que deseas modificar es: \n")
                            print(ver.buscarCliente(r))

                            if ver.buscarCliente(r) == "No se encontro el elemento":
                                break
                            else:
                                for x in range(0, len(ver.regC), 1):

                                    if r == x:
                                        print("\nIngrese los nuevos datos: \n")
                                        ide = input("ID: ")
                                        nom = input("Nombre: ")
                                        rfc = input("RFC: ")
                                        dire = input("Direccion: ")
                                        rem = clientes.clientes()
                                        gua = clientes.clientes()
                                        rem.id = ide
                                        rem.nombre = nom
                                        rem.rfc = rfc
                                        rem.direccion = dire
                                        gua.modificarCliente(rem, r)
                                        print("\nEl cliente ha sido modificado \n")
                                        break

                    elif op2 == 6:

                        print("|****************************|")
                        print("|***********-GUARDAR CLIENTE-*********|")
                        print("|****************************|")
                        gc = clientes.clientes()
                        if gc.regC == []:
                            print("Lista vacia, no hay registros por guardar")
                        else:
                            convC = gc.lisDicC()
                            gc.toJsonC(convC)
                            if gc.toJsonC(convC) == "Archivo creado y datos guardados":
                                print(gc.toJsonC(convC))
                            else:
                                print(gc.toJsonC(convC))

                    elif op2 == 7:

                        break

                    else:

                        print("\n¡Opcion no valida!\n")

                except Exception as exep:

                    print("Error en Clientes, Ingrese bien los datos")

        elif op1 == 2:

            while True:

                print("|****************************|")
                print("|**|      Bienvenidos     |**|")
                print("|**|         Menu         |**|")
                print("|**|    Compañia Guzman   |**|")
                print("|****************************|")
                print("|***********-Articulos-*********|")
                print("|****************************|")
                print("1.- Ingresar articulos\n")
                print("2.- Mostrar articulos\n")
                print("3.- Eliminar articulos\n")
                print("4.- Buscar articulos\n")
                print("5.- Modificar articulos\n")
                print("6.- Guardar articulos\n")
                print("7.- Regresar\n")
                print("|****************************|")
                try:

                    op3 = int(input("Ingrese el numero que desea ejecutar: "))

                    if op3 == 1:

                        print("|****************************|")
                        print("|***********-INGRESAR Articulo-*********|")
                        print("|****************************|")
                        cant = int(input("¿Cuantos articulos desea ingresar? (Ingrese 0 para salir): "))
                        print("\n")
                        for lim in range(0, cant):

                            id_a = input("ID: ")
                            cve_a = input("Clave: ")
                            nom_a = input("Nombre: ")
                            ar = articulos.articulos()
                            ag = articulos.articulos()
                            ar.id = id_a
                            ar.clave = cve_a
                            ar.nom = nom_a
                            ag.agregarArticulo(ar)
                            print("\n")

                        print("\nArticulos agregados")

                    elif op3 == 2:

                        print("|****************************|")
                        print("|***********-Mostrar Articulos-*********|")
                        print("|****************************|")
                        mos = articulos.articulos()
                        if mos.regA == []:
                            print("\nLista vacia")
                        else:
                            for m in mos.imprimirArticulos():
                                print(m)

                    elif op3 == 3:

                        print("|****************************|")
                        print("|***********-Eliminar Articulo-*********|")
                        print("|****************************|")
                        eli = articulos.articulos()
                        if eli.regA == []:
                            print("Lista vacia")
                        else:
                            de = int(input("Ingrese el id a eliminar: "))
                            print("\nArticulo eliminado fue: \n")
                            print(eli.eliminarArticulo(de))

                    elif op3 == 4:

                        print("|****************************|")
                        print("|***********-Buscar Articulo-*********|")
                        print("|****************************|")
                        bu = articulos.articulos()
                        if bu.regA == []:
                            print("Lista vacia")
                        else:
                            be = int(input("Ingrese el ID del cliente que desea buscar: "))
                            print("\nEl articulo que buscabas es: \n")
                            print(bu.buscarArticulo(be))

                    elif op3 == 5:

                        print("|****************************|")
                        print("|***********-Modificar Articulo-*********|")
                        print("|****************************|")
                        ver = articulos.articulos()
                        if ver.regA == []:
                            print("Lista vacia")
                        else:
                            for i in ver.imprimirArticulos():
                                print(i)

                            r = int(input("\nIngrese el ID del cliente que desea modificar: "))
                            print("\nEl articulo que deseas modificar es: \n")
                            print(ver.buscarArticulo(r))

                            if ver.buscarArticulo(r) == "No se encontro el elemento":
                                break
                            else:
                                for x in range(0, len(ver.regA), 1):
                                    if r == x:
                                        print("\nIngrese los nuevos datos: \n")
                                        id_n = input("ID: ")
                                        cve_n = input("Clave: ")
                                        nom_n = input("Nombre: ")
                                        rem = articulos.articulos()
                                        gua = articulos.articulos()
                                        rem.id = id_n
                                        rem.nom = nom_n
                                        rem.clave = cve_n
                                        gua.modificarArticulo(rem, r)
                                        print("\nEl articulo ha sido modificado \n")
                                        break

                    elif op3 == 6:

                        print("|****************************|")
                        print("|***********-Guardar Articulo-*********|")
                        print("|****************************|")
                        g = articulos.articulos()
                        if g.regA == []:
                            print("Lista esta vacia, no hay registros por guardar")
                        else:
                            convertir = g.lisDicA()
                            g.toJsonA(convertir)
                            if g.toJsonA(convertir) == "Archivo creado y datos guardados":
                                print(g.toJsonA(convertir))
                            else:
                                print(g.toJsonA(convertir))

                    elif op3 == 7:
                        break

                    else:

                        print("\n¡Opcion no valida!\n")

                except Exception as exe:

                    print("Error en Articulos, Ingrese bien los datos")

        elif op1 == 3:

            while True:

                print("|****************************|")
                print("|**|      Bienvenidos     |**|")
                print("|**|         Menu         |**|")
                print("|**|    Compañia Guzman   |**|")
                print("|****************************|")
                print("|***********-Venta-*********|")
                print("|****************************|")
                print("1.- Realizar una venta\n")
                print("2.- Mostrar todas las ventas\n")
                print("3.- Buscar una venta\n")
                print("4.- Guardar ventas\n")
                print("5.- Regresar\n")

                try:
                    op4 = int(input("Ingrese el numero que desea ejecutar: "))

                    if op4 == 1:

                        print("\n---------- R E A L I Z A R  -  V E N T A ----------\n")
                        cl = clientes.clientes()
                        ar = articulos.articulos()
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
                            ide_a = int(input("\nID del articulo: "))
                            fecha = input("\nFecha: ")
                            cantidad = int(input("\nCantidad de articulos: "))
                            prec = float(input("\nPrecio del articulo: "))

                            if cl.buscarCliente(ide_c) == "No se encontro el elemento":
                                print(cl.buscarCliente(ide_c))
                            elif ar.buscarArticulo(ide_a) == "No se encontro el elemento":
                                print(ar.buscarArticulo(ide_a))
                            else:
                                v = ventas.ventas()
                                v.id_v = ide_v
                                v.Cliente = cl.buscarCliente(ide_c)
                                v.Articulo = ar.buscarArticulo(ide_a)
                                v.fecha_v = fecha
                                v.cant_a = cantidad
                                v.pre_a = prec
                                v.calculo()
                                myVenta = ventas.ventas()
                                print(v)
                                myVenta.agregarVenta(v)
                                print("\nVenta realizada")

                    elif op4 == 2:

                        print("\n---------- M O S T R A R  -  V E N T A S ----------\n")
                        mosV = ventas.ventas()
                        for mex in mosV.mostrarVentas():
                            print(mex)

                    elif op4 == 3:

                        print("\n---------- B U S C A R  -  V E N T A ----------\n")
                        buscar = ventas.ventas()
                        busc = int(input("Ingrese el ID del cliente que desea buscar: "))
                        print("\nEl articulo que buscabas es: \n")
                        print(buscar.buscarVenta(busc))

                    elif op4 == 4:

                        print("\n---------- G U A R D A R  -  V E N T A S ----------\n")
                        ven = ventas.ventas()
                        if ven.lista == []:
                            print("Lista esta vacia, no hay registros por guardar")
                        else:
                            conVen = ven.lisDicV()
                            ven.JsonV(conVen)

                    elif op4 == 5:

                        break


                    else:
                        print("\n¡Opcion no valida!\n")
                except Exception as excepto:
                    print("Error en Venta, Ingrese bien los datos")

        elif op1 == 4:

            print("\nHasta luego, vuelva pronto\n")
            break

        else:

            print("\n¡Opcion no valida!\n")

    except Exception as ex:

        print("\nError general, Ingrese bien los datos")
