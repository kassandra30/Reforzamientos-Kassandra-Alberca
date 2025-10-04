"""Crear una clase Persona con los siguientes requerimientos.
La clase tendrá como atributos el nombre, edad y sueldo de una persona.
Implementar los métodos necesarios para inicializar los atributos
(constructor), un metodo para mostrar los datos e indicar si la persona es
mayor de edad o no y otro metodo que bonificación que retornará el 20%
adicional de su sueldo, en caso sea mayor de edad. Un metodo para saber
cuántos meses ha estado trabajando en la empresa"""

class Persona:
    def __init__(self, nombre, edad, sueldo, meses_trabajados):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
        self.meses_trabajados = meses_trabajados

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sueldo: {self.sueldo}")
        print(f"Meses trabajando: {self.meses_trabajados}")

    def es_mayor_edad(self):
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} es menor de edad.")

    def bonificacion(self):
        if self.edad >= 18:
            bono = self.sueldo * 0.20
            print(f"Bonificación (20%): {bono}")
        else:
            print("No recibe bonificación por ser menor de edad.")

    def tiempo_trabajando(self):
        print(f"{self.nombre} ha trabajado {self.meses_trabajados} meses en la empresa.")

p1 = Persona("Kass", 24, 1500, 14)
p2 = Persona("Luis", 25, 1200, 8)
p3 = Persona("Leandr", 26, 2000, 24)

for p in [p1, p2, p3]:
    print("\n--- Datos de la persona ---")
    p.mostrar_datos()
    p.es_mayor_edad()
    p.bonificacion()
    p.tiempo_trabajando()