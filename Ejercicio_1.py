"""

Ejercicio 1

Autor: TOBIAS RAFAEL OVIEDO

Grupo: 40

"""

class registro:
    """ Esta clase permite guardar los datos de los clientes de un comercio"""
    
    def __init__(self, nombre, ci, telf):
        """ En el constructor vamos a inicializar las variables que vamos a utilizar en la clase"""
        
        self.nombre = nombre # Inicializamos el atributo nombre
        
        self.ci = ci # Inicializamos el atributo ci
        
        self.telf = telf # Inicializamos el atributo telf 
    def __str__(self):
        """ Esta funcion se encarga de mostrar de forma ordenada y legible el resultado """
        return (
            "====================\n"
            "       CLiente      \n"
            "====================\n" 
            f"Cliente: {self.nombre}\n" 
            f"Cedula:  {self.ci}\n"
            f"Telefono:{self.telf}\n" 
            "====================\n"
        )
cliente_1 = registro('Maria', '8.349.622', '0971 761 715') # Creamos al cliente 1 que sera registrado

cliente_2 = registro('Bruno', '9.450.733', '0982 872 826')# Creamos al cliente 2 que sera registrado
    
print(cliente_1) # Imprimimos la ficha del cliente 1

print(cliente_2) # Imprimimos la ficha del cliente 2