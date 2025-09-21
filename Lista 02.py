"""
Programa que sustituye departamentos en una lista
"""

departamentos = ["Lima", "Arequipa", "Cusco", "Piura", "La Libertad", "Lambayeque"]

print("Departamentos actuales:", departamentos)

# Ingresar departamentos a sustituir
dep_antiguo = input("Ingrese el departamento a reemplazar: ")
dep_nuevo = input("Ingrese el nuevo departamento: ")

# Sustituir si existe
if dep_antiguo in departamentos:
    indice = departamentos.index(dep_antiguo)
    departamentos[indice] = dep_nuevo
    print(f"Lista actualizada: {departamentos}")
else:
    print(f"El departamento '{dep_antiguo}' no existe en la lista")