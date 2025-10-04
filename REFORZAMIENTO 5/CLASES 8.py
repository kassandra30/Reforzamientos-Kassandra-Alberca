"""Escribir una clase Figura que debe tener un atributo de nombre de la
figura.
Habrá otra clase llamada Rectangulo que hereda de Figura. Pedirá una base y
una altura en sus parámetros. Tendrá un metodo que devuelva el área y
perímetro de este rectángulo.
También habrá otra clase llamada Circulo que hereda también de Figura,
pedirá por parámetro el radio y este tendrá los métodos que calculará el área
y otro metodo que calculará el perímetro del círculo
Realizar la instancia de la clase figura mínimo 4 veces para mostrar el uso en
ambas figuras (2 casos para ambas figuras) y resultados de todos los métodos
mediante consola."""

import math

class Figura:
    def __init__(self, nombre):
        self.nombre = nombre

class Rectangulo(Figura):
    def __init__(self, base, altura):
        super().__init__("Rectángulo")
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Circulo(Figura):
    def __init__(self, radio):
        super().__init__("Círculo")
        self.radio = radio

    def area(self):
        return math.pi * self.radio**2

    def perimetro(self):
        return 2 * math.pi * self.radio

# Ejemplos
r1 = Rectangulo(5, 3)
r2 = Rectangulo(8, 4)
c1 = Circulo(4)
c2 = Circulo(6)

print(f"{r1.nombre}: área={r1.area():.2f}, perímetro={r1.perimetro():.2f}")
print(f"{r2.nombre}: área={r2.area():.2f}, perímetro={r2.perimetro():.2f}")
print(f"{c1.nombre}: área={c1.area():.2f}, perímetro={c1.perimetro():.2f}")
print(f"{c2.nombre}: área={c2.area():.2f}, perímetro={c2.perimetro():.2f}")