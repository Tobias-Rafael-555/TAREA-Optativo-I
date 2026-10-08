"""

Ejercicio 7

Autor: TOBIAS RAFAEL OVIEDO

Grupo: 40


"""

class stock_con_alerta:
    """Esta clase realiza un control sobre un producto en un comercio """
    def __init__(self, producto, cantidad, minimo ):
        
        """ Definimos los atributos de la clase en el constructor """
        
        self.producto = producto # En este atributo se guarda el nombre del producto
        
        self.cantidad = cantidad # En este atributo se guarda el stock disponible 
        
        self.minimo = minimo # Con este atributo se define el stock minimo que debe haber
    
    def registro_venta(self, a_comprar):
        
        """ Este metodo registra las compras realizadas """
        
        if self.cantidad - a_comprar >= 0: # Si la resta del stock actual menos la cantidad que se desea comprar es mayor o igual a cero
            
            self.cantidad -= a_comprar # La compra se puede realizar y restamos al stock las unidades que se desean comprar
            
            print(f"Se registro correctamente la compra de {a_comprar} productos") # Mostramos un mensaje indicando que la compra se efectuo de forma correcta
            
            self.control() # Llamamos al metodo de control para indicar si el stock se encuentra en el minimo una vez realizada la compra 
            
        else: # En caso de que la cantidad de productos solicitados para la compra supere el stock disponible
            
            print("No se cuenta con unidades suficientes..") # Arroja un mensaje indicando que no se cuenta con las unidas disponibles
            
    def reposicion(self, agregar):
        
        """Este metodo permite cargar y reponer el stock"""
        
        self.cantidad += agregar  # A la cantidad actual disponible se le suma la nueva carga
        
        print(f"Se agregaron {agregar} unidades ") # Indicamos que la nueva carga ya esta registrada e indicamos la cantidad 
        
        print(f"El stock disponible es de {self.cantidad}") # Mostramos el nuevo stock disponible
        
    def inventario(self):
        """Este metodo muestra el nombre del producto y las unidades disponibles"""
        
        print(f"Producto: {self.producto} | Unidades disponibles: {self.cantidad}")
    def control(self):
        
        """Este metodo controla que el stock este por encima de la minima y arroja un mensaje cuando alcanza el nivel mas bajo """
        
        if self.cantidad <= self.minimo: # Si el stock actual dispoble es menor a la minima 
            
            print("Alerta!!!.Stock por debajo de 3") # Mostramos un mensaje de alerta
    

#############################################
#                Prueba                     #
#############################################

producto = stock_con_alerta('Jabon', 5, 3) # Pasamos los parametros del producto

producto.inventario()  # Mostramos los datos del producto
print("-"*35)

producto.registro_venta(1) # Registramos la venta de una unidad

producto.inventario()# Mostramos los datos del producto
print("-"*35)

producto.registro_venta(10) # Registramos una venta mayor a la cantidad disponible para probar el sistema de control 

producto.inventario # Mostramos los datos del producto
print("-"*35)

producto.reposicion(20) # Reponemos 20 unidades del producto

producto.inventario()# Mostramos los datos del producto
print("-"*35)