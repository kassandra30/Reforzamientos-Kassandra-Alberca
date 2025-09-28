"""1. Pedir dos números positivos mediante terminal al usuario. Mostrar
como salida el número cuya sumatoria de dígitos es el mayor y los números
cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según
sea conveniente."""

def sumatoria_digitos(num):
    return sum(int(d) for d in str(num))

n1 = int(input("Primer número: "))
n2 = int(input("Segundo número: "))

s1, s2 = sumatoria_digitos(n1), sumatoria_digitos(n2)

# Mostrar mayor suma
print(n1 if s1 > s2 else n2, "tiene la mayor sumatoria de dígitos")

# Mostrar los menores que 10
if s1 < 10: print(n1, "→ suma", s1)
if s2 < 10: print(n2, "→ suma", s2)