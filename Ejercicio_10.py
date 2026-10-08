
"""
Ejercicio 10

Autor: TOBIAS RAFAEL OVIEDO 

Grupo: 40

"""



class Producto:
    """Clase que representa un producto con su nombre y precio unitario."""

    def __init__(self, nombre: str, precio: float):
        """Inicializa los atributos básicos del producto."""
        self.nombre = nombre  # Guarda el nombre del producto
        self.precio = precio  # Guarda el precio unitario del producto

    def __str__(self):
        """Devuelve una representación legible del producto."""
        return f"{self.nombre} (Gs. {self.precio:,.0f})"  # Retorna el nombre y el precio formateado


class Item:
    """Clase que representa un ítem dentro del carrito, asociando un producto con su cantidad."""

    def __init__(self, producto: Producto, cantidad: int):
        """Inicializa un ítem con un objeto Producto y la cantidad solicitada."""
        self.producto = producto  # Almacena el objeto Producto asignado
        self.cantidad = cantidad  # Almacena la cantidad de unidades

    def calcular_subtotal(self) -> float:
        """Calcula el subtotal multiplicando el precio del producto por la cantidad."""
        return self.producto.precio * self.cantidad  # Retorna el producto de precio x cantidad

    def __str__(self) -> str:
        """Devuelve el detalle formateado del ítem con su subtotal."""
        return f"{self.producto.nombre} x{self.cantidad} - Subtotal: Gs. {self.calcular_subtotal():,.0f}"  # Formatea la descripción del ítem


class Carrito:
    """Clase que gestiona la colección de ítems seleccionados por el cliente."""

    def __init__(self):
        """Inicializa el carrito con una colección vacía de ítems."""
        self.items = []  # Crea una lista vacía para guardar instancias de Item

    def agregar_item(self, item: Item):
        """Añade un objeto Item al carrito de compras."""
        self.items.append(item)  # Agrega el objeto Item al final de la lista interna

    def calcular_total(self) -> float:
        """Calcula el total general sumando el subtotal de cada ítem."""
        total = 0.0  # Inicializa la variable acumuladora del total en cero
        for item in self.items:  # Recorre cada objeto Item presente en la lista
            total += item.calcular_subtotal()  # Suma el subtotal del ítem al total acumulado
        return total  # Devuelve la suma acumulada total

    def mostrar_detalle(self):
        """Muestra por consola la lista detallada de ítems y el total definitivo a pagar."""
        print("=== Detalle del Carrito de Compras ===")  # Imprime el título del reporte
        if not self.items:  # Evalúa si la lista de ítems está vacía
            print("El carrito se encuentra vacío.")  # Alerta que no hay ítems guardados
            return  # Interrumpe la ejecución del método
        for item in self.items:  # Recorre cada ítem guardado
            print(f"- {item}")  # Imprime la representación __str__ de cada ítem
        print("--------------------------------------")  # Imprime una línea separadora
        print(f"TOTAL A PAGAR: Gs. {self.calcular_total():,.0f}")  # Muestra la suma total a abonar

    def __str__(self) -> str:
        """Devuelve un resumen del estado del carrito con la cantidad de ítems y el total."""
        return f"Carrito con {len(self.items)} producto(s) | Total: Gs. {self.calcular_total():,.0f}"  # Resumen descriptivo


if __name__ == "__main__":
    # Creamos instancias de productos
    prod1 = Producto("Notebook Lenovo", 4500000)  # Instancia el primer producto
    prod2 = Producto("Mouse Inalámbrico", 120000)  # Instancia el segundo producto
    prod3 = Producto("Teclado Mecánico", 350000)   # Instancia el tercer producto

    # Creamos ítems asociando los productos y las cantidades deseada
    item1 = Item(prod1, 1)  # Crea ítem con 1 Notebook
    item2 = Item(prod2, 2)  # Crea ítem con 2 Mouses
    item3 = Item(prod3, 1)  # Crea ítem con 1 Teclado

    # Instanciamos el carrito de compras y agregamos los ítems
    carrito_compras = Carrito()            # Instancia un objeto Carrito
    carrito_compras.agregar_item(item1)    # Agrega el primer ítem al carrito
    carrito_compras.agregar_item(item2)    # Agrega el segundo ítem al carrito
    carrito_compras.agregar_item(item3)    # Agrega el tercer ítem al carrito

    # Visualizamos el desglose de la compra
    carrito_compras.mostrar_detalle()      # Llama al método para imprimir el desglose por consola