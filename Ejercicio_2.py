"""
Ejercicio 2

Autor: TOBIAS RAFAEL OVIEDO 

Grupo: 40

"""
class producto:
    """ Esta clase representa los productos con stock disponible"""
    def __init__(self, nombre, precio, cantidad):
        
         """En el constructor inicializamos los atributos que vamos a utilizar"""
         
         self.nombre = nombre # En el atributo nombre se guardara el nombre del articulo
         
         self.precio = precio  # En el atributo precio se guardara el precio del articulo
         
         self.cantidad = cantidad # En el atributo  cantidad de guardara la cantidad de unidades del mismo articulo 
    def stock_total(self):
        
        """ En este metodo se calcula el valor del total de un producto en especifico """
        
        total = self.precio * self.cantidad # El total es igual a la multiplicacion de la cantidad por el precio
        
        return total # Este metodo devolvera el total
    def __str__(self):
        """ COnvertimos en algo legible con str """
        
        return(
            # Esto es lo que vera el usuario 
            "-----------------------------------------------------------------\n"
            "                              Stock    \n"
            "-----------------------------------------------------------------\n"
            f"Producto:                         {self.nombre:}\n"
            f"Precio:                           {self.precio:,.0f}\n"
            f"Cantidad:                         {self.cantidad:,.0f}\n"
            f"Valor total del stock disponible: {self.stock_total():,.0f}\n"
            "------------------------------------------------------------------"
        )
producto_1 = producto('Bombilla', 5000, 5) # Agregamos el producto 1

producto_2 = producto('Martillo', 50000, 10) # Agregamos el producto 2

producto_3 = producto('Televisor',1500000, 5) # Agregamos el producto 3


print(producto_1) #Imprimimos el resultado 1

print(producto_2) # Imprimimos el resultado 2

print(producto_3) # Imprimimos el resultado 3
