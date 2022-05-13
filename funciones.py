def listarCC(cc):
    print("\nClientes: \n")
    for cur in cc:
        datos = " Código: {0} // Nombre: {1} // Rfc: {2} // Direccion: {3}"
        print(datos.format(cur[0], cur[1], cur[2],cur[3]))

    print(" ")


def pedirDatosRegistro():
    codigoCorrecto = False
    while(not codigoCorrecto):
        id = input("Ingrese Id: ")
        if len(id) == 6:
            codigoCorrecto = True
        else:
            print("Id incorrecto: Debe tener 6 dígitos.")

    nombre = input("Ingrese nombre: ")

    rfc = input("Ingrese rfc: ")
    direccion=input("ingrese direccion:")
    clientes = (id, nombre, rfc,direccion)
    return clientes

def pedirDatosActualizacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEditar = input("Ingrese el Id del cliente a editar: ")
    for cur in cc:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        nombre = input("Ingrese nombre a modificar: ")
        rfc = input("ingrese su rfc:")
        direccion = input("Ingrese la direccion:")
        clientes = (codigoEditar, nombre, rfc ,direccion)
    else:
        clientes = None

    return clientes


def pedirDatosEliminacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEliminar = input("Ingrese el Id del cliente a eliminar: ")
    for cur in cc:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar