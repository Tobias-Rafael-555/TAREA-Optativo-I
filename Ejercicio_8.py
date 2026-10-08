"""
Ejercicio 8

Autor: TOBIAS RAFAEL OVIEDO

Grupo: 40 

"""

class Cancion:
    """ Esta clase permite guarda una nueva cancion """
    def __init__(self, titulo: str, artista: str, duracion_minutos: float):
        
        """ Definimos todos los atributos en el constructor"""
        
        self.titulo = titulo # Este atributo tendra el nombre de la cancion 
        
        self.artista = artista # Este atributo tendra el nombre del artista o compositor 
        
        self.duracion_minutos = duracion_minutos # Este atributo poseera el tiempo que dura la cancion 

    def __str__(self):
        """Este metodo organiza y transforma en algo legible"""
        
        return f"'{self.titulo}' de {self.artista} ({self.duracion_minutos} min)" # Devuelve el nombre de la cancnion, el compositor y el tiempo que dura 


class ListaReproduccion:
    
    """Esta clase tiene la lista de repoduccion o lista de canciones"""
    
    def __init__(self, nombre: str):
        
        """Definimos los atributos en el constructor"""
        
        self.nombre = nombre #Este atributo tendra el nombre de la lista 
        self.canciones = []  # Colección interna para objetos Cancion

    def agregar_cancion(self, cancion: Cancion): #en cancion:Cancion Estamos indicando que el paramtro que vamos pasar es de la clase "Cancion" 
        
        """ Este metodo añade un objeto  de tipo Cancion a la colección interna. """

        self.canciones.append(cancion) # En la lista canciones se guardara un objeto de tipo cancion que posee un titulo, un nombre yuna duracion 

    def calcular_duracion_total(self):
        
        """Recorre la colección y suma la duración total de las canciones."""
        
        duracion_total = 0.0 # Incializamos nuestra variable local en 0.0
        
        for cancion in self.canciones: # Recorremos con bucle la lista de canciones 
            
            duracion_total += cancion.duracion_minutos #La duracion total va a ser igual a la sumatoria de la duracion de las canciones 
            
        return duracion_total # Devuelve la suma de la duracion de las canciones 

    def mostrar_contenido(self):
        
        """Muestra cada canción en la lista y la duración total al final."""
        
        print(f"=== Lista de Reproducción: {self.nombre} ===") #Muestra el nombre de la lista
        
        if not self.canciones: # Si la la lista no esta vacia 
            
            print("La lista de reproducción está vacía.") # Mostramos un mensaje indicando que la lista esta vacia 
            
            return # No devuelve nada 

        for indice, cancion in enumerate(self.canciones, start=1): # Recorre el indice y la cancion. Enumerate genera un numero para cada cancion y start le dice a la funcion que empiece en 1 y no en 0 por defecto
            
            print(f"{indice}. {cancion.titulo} - {cancion.artista} ({cancion.duracion_minutos} min)") # Mostramos todos los detalles

        total_tiempo = self.calcular_duracion_total() # LLamamos al metodo para calcular la duracion 
        
        print(f"-"*40)
        
        print(f"Duración total de la lista: {total_tiempo:.2f} minutos") # Mostramos la duracion 


# Ejercicio de demostración / uso
if __name__ == "__main__": 
    # Instanciamos la lista de reproducción
    mi_playlist = ListaReproduccion("Mis Favoritas")

    # Creamos objetos Cancion
    c1 = Cancion("Pequeños Sueños", "Arbol", 3.92)
    c2 = Cancion("Glory Box", "Portishead", 2.30)
    c3 = Cancion("Fancy", "Iggy Azalea", 1.90)

    # Agregamos las canciones a la lista
    mi_playlist.agregar_cancion(c1)
    mi_playlist.agregar_cancion(c2)
    mi_playlist.agregar_cancion(c3)

    # Mostramos el contenido y la duración total acumulada
    mi_playlist.mostrar_contenido()