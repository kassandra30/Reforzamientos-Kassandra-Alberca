"""
Programa que verifica si un número es múltiplo de otro
"""

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

# Convertir a enteros
entero1 = int(num1)
entero2 = int(num2)

# Verificar si es múltiplo
if entero2 != 0:
    if entero1 % entero2 == 0:
        print(f"{entero1} es múltiplo de {entero2}")
    else:
        print(f"{entero1} NO es múltiplo de {entero2}")
else:
    print("Error: No se puede dividir por cero")