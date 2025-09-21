"""
Programa que elimina un estudiante de la lista
"""
estudiantes = ["Ana", "Carlos", "María", "Luis", "Sofía"]

print("Lista inicial:", estudiantes)

# Ingresar estudiante a eliminar
nombre = input("Ingrese el nombre del estudiante a eliminar: ")

# Eliminar si existe, agregar si no existe
if nombre in estudiantes:
    estudiantes.remove(nombre)
    print(f"'{nombre}' eliminado de la lista")
else:
    print(f"'{nombre}' no se encuentra en la lista, será agregado")
    estudiantes.append(nombre)

# Mostrar lista actualizada
print("Lista actualizada:", estudiantes)