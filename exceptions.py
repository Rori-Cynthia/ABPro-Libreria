class ProductoNoEncontradoError(Exception):
    def __init__(self, mensaje="El producto indicado no se encuentra en el inventario."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class CantidadInsuficienteError(Exception):
    def __init__(self, mensaje="No hay suficiente stock en el inventario para este producto."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class ErrorArchivoInventario(Exception):
    def __init__(self, mensaje="Error al cargar o guardar el inventario."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)