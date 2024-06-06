from abc import ABC, abstractmethod
# Define un método abstracto `procesar_pago(monto)` que debe ser implementado por las clases derivadas.
    # Este método recibe como parámetro el monto pagado por el cliente.
    # Debe devolver `True` si el pago es aprobado y `False` si es rechazado.
# Define una propiedad `descripcion` que devuelve una cadena con la descripción del producto.
# Define un método `mostrar_caracteristicas()` que imprime las características del producto.

class Producto(ABC):
    def __init__(self, nombre, precio, talla, color):
        self.nombre = nombre
        self.precio = precio
        self.talla = talla
        self.color = color

    @abstractmethod
    def procesar_pago(self, monto):
        pass

    @property
    def descripcion(self):
        return f"{self.nombre} - Talla: {self.talla}, Color: {self.color}"

    def mostrar_caracteristicas(self):
        print(f"\n**Características del producto:**")
        print(f"Nombre: {self.nombre}")
        print(f"Precio: ${self.precio}")
        print(f"Talla: {self.talla}")
        print(f"Color: {self.color}")

# Heredan de la clase `Producto`.
# Agregan atributos específicos para cada tipo de prenda:
    # `Camiseta`: `manga` (tipo de manga).
    # `Pantalon`: `tipo` (tipo de pantalón).
# Implementan el método `procesar_pago(monto)` de manera diferente:
    # Validan si el monto pagado coincide con el precio del producto.
    # Si el monto coincide

class Camiseta(Producto):
    def __init__(self, nombre, precio, talla, color, manga):
        super().__init__(nombre, precio, talla, color)
        self.manga = manga

    def procesar_pago(self, monto):
        if monto == self.precio:
            print(f"\nPago aprobado para Camiseta: {self.descripcion}")
            return True
        else:
            print(f"\nPago rechazado para Camiseta: {self.descripcion}")
            return False


class Pantalon(Producto):
    def __init__(self, nombre, precio, talla, color, tipo):
        super().__init__(nombre, precio, talla, color)
        self.tipo = tipo

    def procesar_pago(self, monto):
        if monto == self.precio:
            print(f"\nPago aprobado para Pantalón: {self.descripcion}")
            return True
        else:
            print(f"\nPago rechazado para Pantalón: {self.descripcion}")
            return False


# Ejemplo de uso
camiseta1 = Camiseta("Camiseta básica", 20, "M", "Negro", "Corta")
pantalon1 = Pantalon("Jeans clásico", 35, "32", "Azul", "Casual")

# Mostrar características
camiseta1.mostrar_caracteristicas()  # Imprime las características de la Camiseta 1
pantalon1.mostrar_caracteristicas()  # Imprime las características del Pantalón 1

# Pago para Camiseta
monto_pago_camiseta = 20
resultado_pago_camiseta = camiseta1.procesar_pago(monto_pago_camiseta)

if resultado_pago_camiseta:
    print("Compra de Camiseta realizada con éxito")  # Indica si la compra fue exitosa
else:
    print("Compra de Camiseta fallida")  # Indica si la compra falló

# Pago para Pantalón
monto_pago_pantalon = 35
resultado_pago_pantalon = pantalon1.procesar_pago(monto_pago_pantalon)

if resultado_pago_pantalon:
    print("Compra de Pantalón realizada con éxito")  # Indica si la compra fue exitosa
else:
    print("Compra de Pantalón fallida")  # Indica si la compra falló