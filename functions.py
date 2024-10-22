from menu import imprimir_menu_principal, imprimir_menu_tipos
from clases import Producto, Libro, Revista, Papeleria, Inventario, Venta
from exceptions import ProductoNoEncontradoError
from dataclasses import fields, is_dataclass


def obtener_tipos(tipos_productos_disponibles):
    opciones_tipos = {opcion: tipo.__name__ for opcion, tipo in enumerate(tipos_productos_disponibles, start=1)}
    imprimir_menu_tipos(opciones_tipos)
    return opciones_tipos

#def solicitar_atributos(cls):
    atributos = cls.__init__.__code__.co_varnames[1:]
    variables = {attr: input(f"Ingrese {attr} del nuevo: ") for attr in atributos}
    return variables

def solicitar_atributos(cls):
    atributos = set()

    def obtener_atributos(c):
        if not is_dataclass(c):
            return
        for field in fields(c):
            atributos.add(field.name)
        for base in c.__bases__:
            obtener_atributos(base)

    obtener_atributos(cls)

    if atributos:
        variables = {attr: input(f"Ingrese {attr} del nuevo: ") for attr in atributos}
    else:
        print("No se encontraron atributos para solicitar.")
        variables = {}

    return variables

def run():
    inventario = Inventario()
    inventario.cargar_inventario("inventario.txt")

    while True:
        imprimir_menu_principal()
        try:
            opcion = int(input("La opción elegida es: "))
            if opcion == 1:
                try:
                    codigo = int(input("Ingresa el código del nuevo producto: "))
                    if inventario.buscar_producto(codigo) is not None:
                        print("El producto ya se encuentra ingresado.")
                    else:
                        tipos_productos_disponibles = Producto.__subclasses__()    
                        opciones = obtener_tipos(tipos_productos_disponibles)
                        opcion_tipos = int(input("Ingresa el tipo del nuevo producto: "))
                        atributos_producto = solicitar_atributos(opciones[opcion_tipos])
                        
                except ValueError:
                    print("Entrada no válida. Por favor, ingresa un número del 1 al 7")
                
            elif opcion == 2:
                pass
            elif opcion == 3:
                pass
            elif opcion == 4:
                pass
            elif opcion == 5:
                pass
            elif opcion == 6:
                pass
            elif opcion == 7:
                print("Estas saliendo del sistema ¡Hasta luego!")
                break
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número del 1 al 7")