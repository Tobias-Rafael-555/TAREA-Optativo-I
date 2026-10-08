"""
Ejercicio 4

Autor: TOBIAS RAFAEL OVIEDO 

Grupo: 40

"""
class Biblioteca:
    
    """ Esta clase muestra la ficha y el estado de un libro indicando si esta disponible o ya esta ocupado"""
    
    def __init__(self, titulo, autor, estado=True): 
        """En el constructor inicializamos todas los atributos """
        
        self.titulo = titulo # En este  atributo se guardara el titulo del libro 
         
        self.autor = autor # Este atributo guardara el nombre del autor de este libro 
        
        self.estado = estado # EN la variable estado se indicara si el libro esta disponible o ya se presto
        
    def estado_actual(self):
        """ En este metodo se verifica si el libro esta disponible"""
        
        if self.estado != False: # Si el estado del libro no es False
            
            return "Disponible" # Devuelve un mensaje indicando que el libro si esta disponible
        
        else: # En caso de que el estado del libro sea False 
            
            return "No disponible" # Devuelve un mensaje indicando que el libro no esta disponible 
        
    def __str__(self):
        """Con el metodo str mostramos la infromacion de una forma legible y ordenada"""
        
        return(
            
            f"Titulo: {self.titulo}\n"
            f"Autor:  {self.autor}\n"
            f"Estado: {self.estado_actual()}\n"
        )
libro_1 = Biblioteca('El principe', "Maquiavelo", False) # Cargamos el libro 1

libro_2 = Biblioteca('El principito', 'Desconocido',)  # Cargamos el libro 2 

print(libro_1) # Imprimimos el resultado 1

print(libro_2) # Imprimimos el resultado 2
