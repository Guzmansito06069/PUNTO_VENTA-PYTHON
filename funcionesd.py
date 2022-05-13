import articulosb
import funcionesb


def listarCC(cc):
    print("\nReporte: \n")
    for cur in cc:
        datos = " id: {0} // dia: {1} // iva: {2} // subtotal: {3} // total:{4}"
        print(datos.format(cur[0], cur[1], cur[2],cur[3],cur[4]))

    print(" ")


def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        id = input("Ingrese Id: ")
        if len(id) == 6:
            codigoCorrecto = True
        else:
            print("Id incorrecto: Debe tener 6 dígitos.")

    dia = input("Ingrese el dia: ")

    precio=int(input("Ingresa el precio"))
    cantidad=int(input("Ingrese la cantidad"))

    subtotal = precio * cantidad
    iva = subtotal * 0.16
    importe = iva + subtotal
    listarCC(cc)
    reporte1 = (id,dia,precio,cantidad,subtotal,iva)
    return reporte1

def pedirDatosActualizacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEditar = input("Ingrese el Id del Reporte a editar: ")
    for cur in cc:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        dia = input("Ingrese nombre a modificar: ")

        reporte1 = (codigoEditar, dia, rfc ,direccion)
    else:
        reporte1 = None

    return reporte1


def pedirDatosEliminacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEliminar = input("Ingrese el Id del Reporte a eliminar: ")
    for cur in cc:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar