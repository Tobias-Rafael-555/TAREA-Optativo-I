"""
Ejercicio 5

Autor: TOBIAS RAFAEL OVIEDO

Grupo: 40

"""
class Vehiculo:
    
    """Esta clase debe crear una ficha con la descripción comercial de un vehículo lista para ser publicada"""
    
    def __init__(self, marca, modelo, año, precio):
        
        """ Inicializamos los atributos en el constructor """
        
        self.marca = marca # En este atributo se guardara la marca del vehiculo
        
        self.modelo = modelo # El modelo del vehiculo se guardara en este atributo
        
        self.año = año # El año de vehiculo estara en este atributo
        
        self.precio = precio # Aqui se guarda el precio
        
    def detalle_comercial(self): 
        
        """En este metodo se crear la ficha comercial con los datos solictados """
        
        precio_formateado = f"{self.precio:,}".replace(",", ".") # Reemplazamos las comas por puntos 
        
        anio = f"Año:{self.año}"
        
        return self.marca, self.modelo, anio, precio_formateado # Devolvemos los datos del vehiculo
    
    def __str__(self): 
        """Transformamos en informacion legible y ordenada """
        
        return(
            
        f"Detalles del vehiculo: {self.detalle_comercial()}\n"
        )
vehiculo = Vehiculo('Poyota', 'Aubis', '2000', 45000000 ) # Cargamos el vehiculo 

print(vehiculo) # Mostramos el resultado