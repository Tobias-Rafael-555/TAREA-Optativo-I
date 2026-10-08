"""
Ejercicio 12

Autor: TOBIAS RAFAEL OVIEDO 

Grupo: 40

"""
class CuentaServicio:
    """Clase que controla la línea de telefonía celular y el consumo del paquete de datos."""

    def __init__(self, cliente: str, gigas_plan: float):
        """Inicializa la línea con el cliente titular, límite de gigas y consumo en cero."""
        self.cliente = cliente  # Guarda el nombre del titular del servicio
        self.gigas_plan = gigas_plan  # Asigna el volumen total de gigas contratados
        self.gigas_consumidos = 0.0  # Inicializa el contador de datos consumidos en cero

    def registrar_consumo(self, cantidad_gb: float):
        """Registra un nuevo consumo en GB asegurando que no se supere el total contratado."""
        if cantidad_gb <= 0:  # Valida que el dato de consumo ingresado sea mayor a cero
            print("Error: El consumo a registrar debe ser una cantidad mayor a 0 GB.")  # Imprime aviso
            return  # Abandona el método

        disponibles = self.gigas_disponibles()  # Obtiene el saldo de gigas disponibles

        if disponibles == 0:  # Comprueba si el paquete ya se encuentra agotado
            print(f"AVISO: Paquete agotado. No se puede consumir {cantidad_gb} GB.")  # Muestra alerta de bloqueo
            return  # Impide registrar más consumo

        if cantidad_gb > disponibles:  # Comprueba si el consumo pretendido supera el saldo remanente
            print(f"ALERTA: El consumo excede los {disponibles:.2f} GB disponibles.")  # Notifica exceso
            self.gigas_consumidos = self.gigas_plan  # Agota por completo el límite máximo del plan
            print("Se ha consumido la totalidad del paquete restante.")  # Informa el agotamiento del saldo
        else:  # Si la cantidad solicitada no supera la disponibilidad
            self.gigas_consumidos += cantidad_gb  # Incrementa el acumulador de consumo
            print(f"Consumo registrado con éxito: {cantidad_gb:.2f} GB.")  # Confirma el consumo efectuado

    def gigas_disponibles(self) -> float:
        """Calcula y devuelve la cantidad de gigabytes que quedan en el plan."""
        restante = self.gigas_plan - self.gigas_consumidos  # Resta el consumo realizado del límite del plan
        return max(0.0, restante)  # Devuelve el valor remanente asegurando que no sea menor a cero

    def __str__(self) -> str:
        """Devuelve un estado descriptivo con la información del plan y consumo actual."""
        return (f"Cliente: {self.cliente} | Plan: {self.gigas_plan} GB | "
                f"Consumido: {self.gigas_consumidos:.2f} GB | Libre: {self.gigas_disponibles():.2f} GB")  # Formateo general


if __name__ == "__main__":
    # Creamos la cuenta con un plan de 10 GB
    linea = CuentaServicio("Tobias Oviedo", gigas_plan=10.0)  # Instancia la línea telefónica
    print(linea)  # Muestra el estado inicial antes de consumir datos

    # Simulamos consumos progresivos
    linea.registrar_consumo(3.5)  # Consume 3.5 GB
    print(f"Disponibles: {linea.gigas_disponibles():.2f} GB")  # Muestra gigas libres restantes

    linea.registrar_consumo(5.0)  # Consume 5.0 GB
    print(f"Disponibles: {linea.gigas_disponibles():.2f} GB")  # Muestra gigas libres restantes

    linea.registrar_consumo(3.0)  # Intenta consumir 3.0 GB teniendo solo 1.5 GB disponibles

    linea.registrar_consumo(1.0)  # Intenta realizar un nuevo consumo cuando el paquete ya está agotado
    print(linea)  # Muestra la ficha con el estado final del plan