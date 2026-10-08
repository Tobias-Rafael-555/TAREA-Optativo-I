"""
Ejercicio 3

Autor: TOBIAS RAFAEL OVIEDO

Grupo: 40

"""

class Empleado:
  
    """ Esta clase ordena y muestra los da3tos de los empleados incluyendo su salario anual"""
    
    def __init__(self, nombre, cargo, salario_mens): 
        
        """Inicializamos los atributos de la clase en este constructor"""
        
        self.nombre = nombre # El nombre del empleado se guardara en el atributo nombre
        
        self.cargo = cargo # El puesto del empleado se guardara en el atributo cargo
        
        self.salario = salario_mens # En este atributo se guardara el salario del empleado 
        
    def salario_anual(self):
        """ Este metodo calcula el salario anual del empleado incluyendo el aguinaldo"""
        
        return self.salario * 13 # Retorna el salario anual mas el aguinalado 
    
    def __str__(self):
        """Devuelve la informacion de forma ordenada y legible"""
        return(
            "=====================================================\n"
            "                  Datos de empleados \n"
            "=====================================================\n"
            f"Nombre:                    {self.nombre}\n"
            f"Cargo:                     {self.cargo}\n"
            f"salario mensual:           {self.salario:,.0f}\n"
            f"Salario anual + Aguinaldo: {self.salario_anual():,.0f}\n"
            
        )
        
empleado_1 = Empleado('Rigoberto', 'Secretario', 3200000) # Creamos al empleado 1 

Empleado_2 = Empleado('Wilma', 'Gerente General', 13500000) # Creamos al empleado 2 

print(empleado_1) # Mostramos los datos del empleado uno

print(Empleado_2) # Mostramos los datos del empleado dos 