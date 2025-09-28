"""
Programa que calcula el Índice de Masa Corporal (IMC)
"""
nombre = input("Ingrese su nombre: ")
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))

# Cálculo del IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print(f"{nombre}, tu Índice de Masa Corporal (IMC) es: {imc:.2f}")