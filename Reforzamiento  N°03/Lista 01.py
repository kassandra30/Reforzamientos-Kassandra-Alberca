"""
Programa que crea una lista de nombres de alumnos
"""
tamano = int(input("Ingrese el tamaño de la lista: "))
alumnos = []

# Ingresar nombres
for i in range(tamano):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    alumnos.append(nombre)

# Mostrar resultados
print(f"\nTamaño de la lista: {len(alumnos)}")
print("Nombres ingresados:")
for alumno in alumnos:
    print(f"- {alumno}")