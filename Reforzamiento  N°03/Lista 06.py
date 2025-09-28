"""
Programa que reorganiza una lista de invitados según criterios específicos
"""
guests = ["Ana", "Katherine", "Pedro", "Luis", "Radi", "Fiorella", "Miguel"]

# Separar en impares y pares según posición
impares = []
pares = []

for i, nombre in enumerate(guests):
    if i % 2 == 0:  # Posición impar (0-based index)
        impares.append(nombre)
    else:  # Posición par
        pares.append(nombre)

# Reorganizar: primero impares, luego pares
reorganizada = impares + pares

print("Lista original:", guests)
print("Lista reorganizada:", reorganizada)