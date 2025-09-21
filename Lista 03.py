"""
Programa que calcula suma y media de 10 números
"""
numeros = []

# Ingresar 10 valores
for i in range(10):
    numero = float(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)

# Calcular suma y media
suma = sum(numeros)
media = suma / len(numeros)

# Mostrar resultados
print(f"\nLista de números: {numeros}")
print(f"Suma: {suma}")
print(f"Media: {media:.2f}")