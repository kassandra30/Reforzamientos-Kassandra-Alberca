"""Crear una clase llamada Circulo que contenga radio en su constructor y
que contenga un metodo área que devuelva el area de un círculo.
Adicionalmente habrá un metodo que devuelva el perímetro del círculo.
También habrá un metodo donde pedirá el radio del círculo.
Instanciar mínimo 2 veces la clase y mostrar resultados por consola."""

import math

class Circulo:
    def __init__(self):
        self.radio = 0

    def pedir_radio(self):
        self.radio = float(input("Ingrese el radio del círculo: "))

    def area(self):
        return math.pi * (self.radio ** 2)

    def perimetro(self):
        return 2 * math.pi * self.radio

print("=== CÍRCULO 1 ===")
c1 = Circulo()
c1.pedir_radio()
print("Área:", round(c1.area(), 2))
print("Perímetro:", round(c1.perimetro(), 2))

print("\n=== CÍRCULO 2 ===")
c2 = Circulo()
c2.pedir_radio()
print("Área:", round(c2.area(), 2))
print("Perímetro:", round(c2.perimetro(), 2))