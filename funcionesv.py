def listarCC(cc):
    print("\nVentas: \n")
    for cur in cc:
        datos = " Código: {0} // id cliente: {1} // id articulo: {2} // fecha: {3} // precio: {4},// total: {5} "
        print(datos.format(cur[0], cur[1], cur[2],cur[3],cur[4],cur[5]))

    print(" ")


def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        id = input("Ingrese Id: ")
        if len(id) == 6:
            codigoCorrecto = True
        else:
            print("Id incorrecto: Debe tener 6 dígitos.")

    idc = input("Ingrese el id del cliente: ")

    ida=input("Ingrese el id del articulo")
    fecha=input("ingrese la fecha:")
    precio = int(input("ingrese la fecha:"))
    x=precio*0.16
    total=x+precio
    venta = (id, idc, ida,fecha,precio,total)
    return venta

def pedirDatosActualizacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEditar = input("Ingrese el Id del cliente a editar: ")
    for cur in cc:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        idc = input("Ingrese el id del cliente: ")

        ida = input("Ingrese el id del articulo")
        fecha = input("ingrese la fecha:")
        precio = int(input("ingrese la fecha:"))
        x = precio * 0.16
        total = x + precio
        venta = (codigoEditar, idc, ida, fecha, precio, total)
    else:
        venta = None

    return venta


def pedirDatosEliminacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEliminar = input("Ingrese el Id de la venta a eliminar: ")
    for cur in cc:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar