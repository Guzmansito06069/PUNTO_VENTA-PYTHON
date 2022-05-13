def listarCC(cc):
    print("\nArticulos: \n")
    for cur in cc:
        datos = " Id: {0} // Codigo: {1} // Nombre: {2} // Precio: {3}"
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
    codigo = input("Ingrese codigo: ")
    nombre = input("Ingrese nombre: ")
    precio=int(input("ingrese el precio:"))
    articulos = (id,codigo, nombre,precio)
    return articulos

def pedirDatosActualizacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEditar = input("Ingrese el Id del articulo a editar: ")
    for cur in cc:
        if cur[0] == codigoEditar:
            existeCodigo = True
            break

    if existeCodigo:
        codigo = input("Ingrese codigo: ")
        nombre = input("Ingrese nombre: ")

        precio = int(input("ingrese precio:"))
        articulos = (codigoEditar, codigo, nombre, precio)
    else:
        articulos = None

    return articulos


def pedirDatosEliminacion(cc):
    listarCC(cc)
    existeCodigo = False
    codigoEliminar = input("Ingrese el Id del Articulo a eliminar: ")
    for cur in cc:
        if cur[0] == codigoEliminar:
            existeCodigo = True
            break

    if not existeCodigo:
        codigoEliminar = ""

    return codigoEliminar