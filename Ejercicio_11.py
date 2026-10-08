"""
Ejercicio 11

Autor: TOBIAS RAFAEL OVIEDO 

Grupo: 40

"""

class Estudiante:
    """Clase que representa a un estudiante y gestiona su historial académico de notas."""

    def __init__(self, nombre: str, nota_minima_aprobacion: float = 60.0):
        """Inicializa los datos personales, la nota mínima requerida y la colección de notas."""
        self.nombre = nombre  # Almacena el nombre completo del estudiante
        self.nota_minima_aprobacion = nota_minima_aprobacion  # Define la calificación mínima para aprobar
        self.notas = {}  # Inicializa un diccionario vacío para los pares 'materia: nota'

    def registrar_nota(self, materia: str, nota: float):
        """Registra o actualiza la calificación obtenida en una materia."""
        if 0 <= nota <= 100:  # Comprueba que la calificación esté en el rango válido de 0 a 100
            self.notas[materia] = nota  # Asigna la nota a la clave de la materia correspondiente
        else:  # Caso en el que la nota no cumpla la validación
            print(f"Error: La calificación {nota} ingresada para '{materia}' fuera de rango.")  # Muestra aviso

    def calcular_promedio(self) -> float:
        """Calcula el promedio general dividiendo la suma total de calificaciones por la cantidad de materias."""
        if not self.notas:  # Verifica si no existen notas registradas
            return 0.0  # Retorna cero si la colección está vacía
        suma_total = sum(self.notas.values())  # Realiza la suma de todas las calificaciones
        return suma_total / len(self.notas)  # Retorna la media aritmética

    def esta_aprobado(self) -> bool:
        """Indica si el promedio obtenido alcanza o supera la nota mínima de aprobación."""
        return self.calcular_promedio() >= self.nota_minima_aprobacion  # Evalúa la condición booleana

    def mostrar_boletin(self):
        """Muestra en pantalla el boletín académico detallado, el promedio global y la condición final."""
        print(f"=== Boletín Académico: {self.nombre} ===")  # Imprime la cabecera del boletín
        if not self.notas:  # Valida si existen materias registradas
            print("No se registran materias cargadas hasta el momento.")  # Alerta ausencia de notas
            return  # Finaliza el procedimiento
        for materia, nota in self.notas.items():  # Recorre los pares de materia y nota
            print(f"- {materia}: {nota:.1f}")  # Imprime el nombre de la materia con su nota
        promedio = self.calcular_promedio()  # Almacena el promedio obtenido
        condicion = "APROBADO" if self.esta_aprobado() else "REPROBADO"  # Establece la condición según el resultado
        print("---------------------------------------")  # Imprime separador estético
        print(f"Promedio General: {promedio:.2f}")  # Muestra el valor numérico del promedio
        print(f"Condición Final: {condicion}")  # Imprime si el estudiante aprobó o no

    def __str__(self) -> str:
        """Devuelve una ficha en texto con el promedio y estado actual del estudiante."""
        estado = "Aprobado" if self.esta_aprobado() else "Reprobado"  # Convierte la condición en cadena
        return f"Estudiante: {self.nombre} | Promedio: {self.calcular_promedio():.2f} | Estado: {estado}"  # Ficha sintética


if __name__ == "__main__":
    # Instanciamos al estudiante definiendo una nota mínima de 60
    alumno = Estudiante("Tobias Oviedo", nota_minima_aprobacion=60.0)  # Crea la instancia del estudiante

    # Carga de materias y calificaciones
    alumno.registrar_nota("Programación Orientada a Objetos", 95.0)  # Registra la nota de POO
    alumno.registrar_nota("Cálculo Diferencial", 82.0)               # Registra la nota de Cálculo
    alumno.registrar_nota("Bases de Datos I", 88.0)                 # Registra la nota de Base de Datos
    alumno.registrar_nota("Redes de Computadoras", 75.0)             # Registra la nota de Redes

    # Impresión del boletín completo
    alumno.mostrar_boletin()  # Llama al método para imprimir el informe en consola