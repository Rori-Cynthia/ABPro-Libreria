from dataclasses import dataclass, asdict
from datetime import date
from exceptions import ProductoNoEncontradoError, CantidadInsuficienteError, ErrorArchivoInventario
from typing import Any
import json

@dataclass
class Producto:
    codigo: int
    nombre: str
    precio: float
    cantidad: int

    def __str__(self):
        return (
            f'Codigo: {self.codigo}, '
            f'nombre: "{self.nombre}", '
            f'precio: ${self.precio}, '
            f'stock: {self.cantidad}'
        )


@dataclass
class Libro(Producto):
    autor: str
    editorial: str


@dataclass
class Revista(Producto):
    numero_de_edicion: str
    fecha_publicacion: date


@dataclass
class Papeleria(Producto):
    pass


@dataclass
class Venta():
    producto: Producto
    cantidad: int

    def calcular_total(self):
        total_venta = self.producto.precio * self.cantidad
        return total_venta


class Inventario():
    productos: list[Producto]

    def __init__(self):
        self.productos = []


    def buscar_producto(self, codigo: int):
        for producto in self.productos:
            if codigo == producto.codigo:
                return producto
        return None


    def agregar_producto(self, nuevo_producto: Producto):
        producto = self.buscar_producto(nuevo_producto.codigo)
        if producto is not None:
            return
        self.productos.append(nuevo_producto)
        

    def eliminar_producto(self, producto: Producto):
        producto = self.buscar_producto(producto.codigo)
        if producto is None:
            raise ProductoNoEncontradoError
        self.productos.remove(producto)


    def modificar_producto(self, codigo: int, dato_a_modificar: str, nuevo_valor: Any):
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ProductoNoEncontradoError
        setattr(producto, dato_a_modificar, nuevo_valor)


    def registrar_venta(self, codigo: int, cantidad: int):
        producto = self.buscar_producto(codigo)
        
        if producto is None:
            raise ProductoNoEncontradoError
        
        if producto.cantidad < cantidad:
            raise CantidadInsuficienteError
                
        venta = Venta(producto, cantidad)
        producto.cantidad -= cantidad


    def guardar_inventario(self, nombre_archivo: str):
        datos = []
        try:
            for producto in self.productos:
                producto_dict = asdict(producto)
                producto_dict['tipo_producto'] = producto.__class__.__name__
                if isinstance(producto, Revista):
                    producto_dict['fecha_publicacion'] = producto.fecha_publicacion.isoformat()
                datos.append(producto_dict)

            with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
                json.dump(datos, archivo, indent=4)
        except:
            raise ErrorArchivoInventario

    def cargar_inventario(self, nombre_archivo: str):
        try:
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                data = json.load(archivo)

            self.productos = []
            for producto_dict in data:
                clase = producto_dict.pop('tipo_producto')
                if clase == 'Revista':
                    producto_dict['fecha_publicacion'] = date.fromisoformat(producto_dict['fecha_publicacion'])  
                producto = globals()[clase](**producto_dict)
                self.productos.append(producto)
        except FileNotFoundError:
            pass
        except:
            raise ErrorArchivoInventario


#bloque de prueba
inventario = Inventario()
inventario.cargar_inventario("inventario.txt")
print(inventario.productos)
# Agregar un producto
libro = Libro(codigo=101, nombre="Python para Todos", precio=15.99, cantidad=10, autor="Juan Pérez", editorial="TechBooks")
inventario.agregar_producto(libro)
# Guardar el inventario en un archivo
inventario.guardar_inventario("inventario.txt")
#Registrar Venta
try:
    inventario = Inventario()
    inventario.cargar_inventario("inventario.txt")
    # Registrar una venta
    inventario.registrar_venta(101, 2) # Vender 2 unidades del producto con código 101
    # Guardar cambios en el inventario
    inventario.guardar_inventario("inventario.txt")
except ProductoNoEncontradoError as e:
    print(f"Error: {e}")
except CantidadInsuficienteError as e:
    print(f"Error: {e}")
except ErrorArchivoInventario as e:
    print(f"Error al manejar el archivo del inventario: {e}")
print(inventario.productos)