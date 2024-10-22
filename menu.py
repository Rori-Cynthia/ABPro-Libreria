def imprimir_menu_principal():
    print("-------------------------------------------------")
    print("Bienvenido al sistema ABPRO.")
    print("Sistema de Gestión de Inventario de Librería")
    print(".................................................")
    print("Porfavor indique la operación que desea realizar:")
    print("1.- Agregar producto")
    print("2.- Eliminar producto")
    print("3.- Modificar producto")
    print("4.- Registrar venta")
    print("5.- Guardar inventario")
    print("6.- Cargar inventario")
    print("7.- Salir")
    print("-------------------------------------------------")

def imprimir_menu_tipos(opciones_tipos):
    print(".................................................")
    print("Porfavor, indique el tipo de producto: ")
    for key, value in opciones_tipos.items():
        print(f"{key}. {value}")