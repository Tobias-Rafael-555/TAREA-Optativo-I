"""
Ejercicio 6

Autor: TOBIAS RAFAEL OVIEDO

Grupo: 40 

""" 

class Cuenta_corriente:
    
    """Esta clasa permite depositar dinero en una cuenta corriente y tambien registrar los gastos de los consumos"""
    
    def __init__(self, cliente=str, saldo_inicial=0):
        
        """ Definimos los atributos en el constrcutor """
        
        self.cliente = cliente # Ete atributo poseera el nombre del cliente 
        
        self.saldo = saldo_inicial # Este atributo tendra el saldo con el que empieza la cuenta corriente que por defecto es Gs.0 
    def acreditacion(self, credito):
        
        """ Este metodo permite acreditar saldo a la cuenta corriente del cliente"""
        
        a_acreditar = credito # esta es una variable local que toma el valor del parametro credito para trabajar con el(es innesario pero por una confusion me seria mas practico dejarlo ahi jeje)
        
        if a_acreditar > 0: # Si el saldo a depositar en mayor a cero 
            
            self.saldo += a_acreditar #El monto a depositar se suma al saldo actual 
            
            print(f"Se acredito correctamente la suma de Gs.{a_acreditar:.0f}") # Mostramos un mensaje indicando que el saldo fue depositado y tambien el monto 
            
        else: # En caso de que el valor ingresado sea menor o igual a cero 
            
            print("Ingrese un monto valido..") # Mostramos un mensaje indicando que que debe ingresar un monto valido
            
    def registrar_consumo(self, monto):
        
        """En este metodo se registrara el consumo o gasto realizado con la cuenta corriente dentro del establecimiento"""
        
        if monto > self.saldo: # Si es que el valor del producto o servicio supera el monto disponible en la cuenta
            
            print("Saldo insuficiente..") # Mostramos un mensaje indicando el problema
            
        else: # En caso de que no haya inconveniente 
            
            self.saldo -= monto # AL saldo actual le restamos el monto o valor del gasto consumo 
            
            print("Se registro el consumo de forma correcta") # Mostramos un mensaje indicando que se registro de forma correcta 
            
            print(f"Saldo actual: {self.saldo}") # Mostramos el saldo actual restante despues de la compra 
            
    def estado(self):
        """Este metodo nos permitira ver el estado del cliente"""
        
        print(f"Cliente: {self.cliente} | Saldo: {self.saldo}") # Mostramos un mensaje con el nombre y el saldo del cliente 
        
##########################################################################

#                                Seccion de prueba

##########################################################################

cuenta = Cuenta_corriente('Tobias',) # Cargamos el nombre del cliente y dejamos el saldo con su valor por defecto

cuenta.estado() #LLamamos al metodo estado para ver los datos de la cuenta
print("-"*34)

cuenta.acreditacion(100000) # Acreditamos  Gs. 100.000 
cuenta.estado() # Volvemos a mostrar el estado de la cuenta despues de la acreditacion 
print("-"*34)

cuenta.registrar_consumo(50000) # Registramos un primer consumo de Gs. 50.000 
cuenta.estado() # Volvemos a mostrar el estado de la cuenta incluyendo el descuento 
print("-"*34)

cuenta.registrar_consumo(200000) # Intentamos registrar un gasto superior al saldo actual para probar 
print("-"*34)
