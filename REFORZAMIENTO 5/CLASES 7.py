"""Crear una clase Persona que contenga dos atributos: nombre y edad.
Nombre y edad se ingresarán por teclado en el constructor.
Declarar una segunda clase llamada Empleado que herede de la clase Persona
y agregue un atributo sueldo. Crearás un metodo que indicará si debe pagar
impuestos (que sería el 10% de su sueldo y si sueldo es superior a 4000 soles)
Instanciar la clase Empleado al menos para 3 empleados, mostrar el sueldo
del empleado y cuánto debe pagar de impuesto."""

class Persona:
    def __init__(self):
        self.nombre = input("Ingrese el nombre de la persona: ")
        self.edad = int(input("Ingrese la edad: "))


class Empleado(Persona):
    def __init__(self):
        # Llamamos al constructor de la clase Persona
        super().__init__()
        self.sueldo = float(input("Ingrese el sueldo del empleado: "))

    def pagar_impuesto(self):
        if self.sueldo > 4000:
            impuesto = self.sueldo * 0.10
            print(f"\nEmpleado: {self.nombre}")
            print(f"Sueldo: S/ {self.sueldo:.2f}")
            print(f"💰 Debe pagar impuestos: S/ {impuesto:.2f}\n")
        else:
            print(f"\nEmpleado: {self.nombre}")
            print(f"Sueldo: S/ {self.sueldo:.2f}")
            print("✅ No paga impuestos.\n")

print("=== Registro de empleados ===")
empleado1 = Empleado()
empleado2 = Empleado()
empleado3 = Empleado()

# Mostramos si pagan impuestos
print("\n=== Resultados ===")
empleado1.pagar_impuesto()
empleado2.pagar_impuesto()
empleado3.pagar_impuesto()