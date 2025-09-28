"""Ingresar por consola 4 números mediante consola, crear un diccionario
donde los ‘key’ serán los números indicados y los valores serán los cubos de
las estos keys. Mostrar finalmente este diccionario."""


cubos = {}

for i in range(4):
    num = int(input(f"Ingrese el número {i+1}: "))
    cubos[num] = num ** 3  # key = número, valor = cubo

# Mostrar el diccionario final
print("Diccionario con cubos:", cubos)