"""
Programa que formatea un número decimal con diferentes precisiones
"""
numero = float(input("Ingrese un número decimal (con 6 decimales): "))

# Mostrar con diferentes precisiones
print(f"1 decimal: {numero:.1f}")
print(f"2 decimales: {numero:.2f}")
print(f"4 decimales: {numero:.4f}")