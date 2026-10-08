"""
Ejercicio 9

Autor: TOBIAS RAFAEL OVIEDO 

Grupo: 40

"""

# Define la clase Turno para modelar cada turno del consultorio
class Turno:
    
    """Método constructor que inicializa un objeto Turno con el paciente y la hora"""
    
    def __init__(self, paciente: str, hora: str):
        
        self.paciente = paciente  # Guarda el nombre del paciente en el atributo de la instancia
        
        self.hora = hora          # Guarda el horario asignado en el atributo de la instancia
        
        self.estado = "pendiente" # Asigna el valor por defecto "pendiente" al atributo estado


    def marcar_como_atendido(self):
        
        """"Método para modificar el estado del turno"""
        
        self.estado = "atendido"  # Actualiza el atributo estado cambiando su valor a "atendido"


    def __str__(self):
        """Método especial que define la representación en texto del objeto Turno"""
        
        return f"Paciente: {self.paciente} | Hora: {self.hora} | Estado: {self.estado}"# Retorna una cadena con la información formateada del turno


# Define la clase Agenda para administrar la colección de turnos del día
class Agenda:
    
    def __init__(self):
        
        """Método constructor que inicializa la agenda"""
        
        self.turnos = []  # Crea una lista vacía para almacenar los objetos Turno

    def agendar_turno(self, turno: Turno):
        
        """Método para registrar un turno en la agenda"""
        
        self.turnos.append(turno)  # Añade el objeto Turno recibido al final de la lista interna

    def listar_pendientes(self):
        
        """# Método para filtrar e imprimir los turnos que no han sido atendidos aún"""
        
        print("=== Turnos Pendientes ===")  # Muestra el encabezado en consola
        
        
        pendientes = [t for t in self.turnos if t.estado == "pendiente"]# Filtra la lista creando una nueva solo con los turnos cuyo estado sea "pendiente"

        
        if not pendientes:# Evalúa si la lista filtrada no tiene elementos
            
            print("No hay turnos pendientes para el día de hoy.")  # Avisa si la lista está vacía
            
            return  # Interrumpe la ejecución del método de forma anticipada

        
        for indice, turno in enumerate(pendientes, start=1):# Recorre los turnos pendientes asignando un número de posición comenzando desde 1
            
            # Imprime el número del turno, el nombre del paciente y su horario
            
            print(f"{indice}. {turno.paciente} - {turno.hora}")



if __name__ == "__main__":
    mi_agenda = Agenda()  # Instancia un nuevo objeto de la clase Agenda

    # Instanciación de 4 objetos de la clase Turno
    t1 = Turno("Ana Gómez", "09:00")       # Crea la instancia para Ana Gómez
    
    t2 = Turno("Carlos Pérez", "09:30")     # Crea la instancia para Carlos Pérez
    
    t3 = Turno("María Rodríguez", "10:00")  # Crea la instancia para María Rodríguez
    
    t4 = Turno("Lucas Silva", "10:30")      # Crea la instancia para Lucas Silva

    # Agregado de las instancias de Turno a la lista interna de la agenda
    mi_agenda.agendar_turno(t1)  # Inserta t1 en la agenda
    
    mi_agenda.agendar_turno(t2)  # Inserta t2 en la agenda
    
    mi_agenda.agendar_turno(t3)  # Inserta t3 en la agenda
    
    mi_agenda.agendar_turno(t4)  # Inserta t4 en la agenda

    # Modificación del estado de los objetos t1 y t3
    
    t1.marcar_como_atendido()  # Ejecuta el método que cambia el estado de t1 a "atendido"
    
    t3.marcar_como_atendido()  # Ejecuta el método que cambia el estado de t3 a "atendido"

    # Invocación del método para mostrar por pantalla los turnos que siguen en "pendiente"
    mi_agenda.listar_pendientes()
