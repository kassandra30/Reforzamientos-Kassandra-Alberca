"""Crear una clase Empleado que contenga los siguientes métodos, uno que
pida ingresar un nombre, apellido y edad, un metodo para pedir su sueldo
actual y otro metodo que lo imprima ambos resultados, pero estarán
contenidos en un diccionario. Comprobar los métodos instanciado la clase
respectivamente al menos para 3 empleados. Considerar en el constructor los
valores necesarios."""

class Empleado:
    def __init__(self):
        self.datos = {}

    def pedir_datos(self):
        self.datos["nombre"] = input("Nombre: ")
        self.datos["apellido"] = input("Apellido: ")
        self.datos["edad"] = int(input("Edad: "))

    def pedir_sueldo(self):
        self.datos["sueldo"] = float(input("Sueldo actual: "))

    def mostrar(self):
        print(self.datos)

empleado1 = Empleado()
empleado1.pedir_datos()
empleado1.pedir_sueldo()
empleado1.mostrar()

empleado2 = Empleado()
empleado2.pedir_datos()
empleado2.pedir_sueldo()
empleado2.mostrar()

empleado3 = Empleado()
empleado3.pedir_datos()
empleado3.pedir_sueldo()
empleado3.mostrar()