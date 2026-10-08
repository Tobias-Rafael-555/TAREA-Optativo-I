"""
Ejercicio 13

Autor: TOBIAS RAFAEL OVIEDO 

Grupo: 40

"""
class Habitacion:
    """Clase que representa una habitación de hotel y administra su disponibilidad."""

    def __init__(self, numero: int, tipo: str, tarifa_noche: float):
        """Inicializa la habitación con su número, tipo, tarifa nocturna y estado libre."""
        self.numero = numero  # Asigna el número identificador de la habitación
        self.tipo = tipo  # Especifica la categoría (ej. 'Simple', 'Suite')
        self.tarifa_noche = tarifa_noche  # Guarda la tarifa cobrada por cada noche
        self.ocupada = False  # Bandera del estado inicial: False representa libre

    def ocupar(self):
        """Modifica el estado de la habitación a ocupada validando su disponibilidad previa."""
        if self.ocupada:  # Verifica si la habitación ya se encuentra habitada
            print(f"Error: La habitación N° {self.numero} ya se encuentra ocupada.")  # Notifica conflicto
        else:  # Caso en el que la habitación esté disponible
            self.ocupada = True  # Cambia el estado a ocupado (True)
            print(f"Éxito: Habitación N° {self.numero} ocupada correctamente.")  # Confirma la operación

    def liberar(self):
        """Modifica el estado de la habitación a libre validando que esté efectivamente ocupada."""
        if not self.ocupada:  # Verifica si la habitación no está ocupada
            print(f"Error: La habitación N° {self.numero} ya está libre.")  # Notifica que ya estaba desocupada
        else:  # Caso en el que la habitación esté ocupada
            self.ocupada = False  # Restablece la bandera de estado a desocupada (False)
            print(f"Éxito: Habitación N° {self.numero} ha sido liberada.")  # Confirma la desocupación

    def calcular_costo_estadia(self, noches: int) -> float:
        """Calcula el costo total de la estadía multiplicando el número de noches por la tarifa nocturna."""
        if noches <= 0:  # Valida que la cantidad de noches ingresada sea válida
            print("Error: La cantidad de noches debe ser como mínimo 1.")  # Muestra aviso
            return 0.0  # Retorna cero por entrada no válida
        return self.tarifa_noche * noches  # Devuelve el cálculo final tarifa x noches

    def __str__(self) -> str:
        """Devuelve una descripción legible con las características y el estado de la habitación."""
        estado_str = "Ocupada" if self.ocupada else "Libre"  # Traduce el valor booleano a texto descriptivo
        return f"Habitación N° {self.numero} ({self.tipo}) | Tarifa: Gs. {self.tarifa_noche:,.0f}/noche | Estado: {estado_str}"  # Retorna el formato


if __name__ == "__main__":
    # Instanciamos la habitación
    hab101 = Habitacion(numero=101, tipo="Matrimonial Deluxe", tarifa_noche=350000)  # Instancia la habitación 101
    print(hab101)  # Muestra el estado inicial (Libre)

    # Simulación del ciclo de vida
    hab101.ocupar()  # Ocupa la habitación
    hab101.ocupar()  # Intenta reocupar la misma habitación para comprobar las validaciones de estado

    dias_estadia = 3  # Define un periodo de reservación de 3 noches
    costo = hab101.calcular_costo_estadia(dias_estadia)  # Ejecuta el cálculo del monto acumulado
    print(f"Costo acumulado por {dias_estadia} noches: Gs. {costo:,.0f}")  # Muestra el monto total a pagar

    hab101.liberar()  # Libera la habitación
    hab101.liberar()  # Intenta reliberar para validar nuevamente las excepciones de estado
    print(hab101)  # Imprime el estado final actualizado de la habitación