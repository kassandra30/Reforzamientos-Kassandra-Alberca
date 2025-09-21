"""
Programa que convierte soles a dólares con tres montos diferentes
"""

tipo_cambio = 3.75  # Tipo de cambio soles a dólares

# Tres montos diferentes a convertir
monto1 = 100
monto2 = 250
monto3 = 500

# Conversiones
dolares1 = monto1 / tipo_cambio
dolares2 = monto2 / tipo_cambio
dolares3 = monto3 / tipo_cambio

# Mostrar resultados
print(f"{monto1} soles = {dolares1:.2f} dólares")
print(f"{monto2} soles = {dolares2:.2f} dólares")
print(f"{monto3} soles = {dolares3:.2f} dólares")