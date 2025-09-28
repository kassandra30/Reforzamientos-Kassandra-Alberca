"""
Programa que elimina duplicados de una lista
"""
tamano = int(input("Ingrese el tamaño de la lista: "))
companias = []

# Ingresar compañías
for i in range(tamano):
    compania = input(f"Ingrese la compañía TI {i+1}: ")
    companias.append(compania)

# Crear copia con duplicados adrede
copia = companias.copy()
print("\nAhora agregaremos algunos nombres repetidos:")
for i in range(3):
    repetido = input(f"Ingrese nombre repetido {i+1}: ")
    copia.append(repetido)

# Eliminar duplicados
sin_duplicados = list(set(copia))

# Mostrar resultados
print(f"\nLista inicial: {companias}")
print(f"Lista con duplicados: {copia}")
print(f"Lista sin duplicados: {sin_duplicados}")