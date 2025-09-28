"""Realizar un programa donde se ingresarán por consola los nombres de los
alumnos (indicar previamente la cantidad de alumnos a ingresar) de un curso y
las notas de c/u. Guardarás la información en un diccionario donde las claves
serán los nombres de c/u de estos alumnos y sus valores serán las notas de
esto alumnos.
Finalmente mostrarás los alumnos con sus notas en un mensaje similar a
“Pedro tiene la nota de 15” y también la media de todas las notas."""

alumnos = {}

n = int(input("¿Cuántos alumnos vas a ingresar?: "))

for i in range(n):
    nombre = input(f"Nombre del alumno {i+1}: ")
    nota = float(input(f"Nota de {nombre}: "))
    alumnos[nombre] = nota

for nombre, nota in alumnos.items():
    print(f"{nombre} tiene la nota de {nota}")

media = sum(alumnos.values()) / len(alumnos)
print("La media de las notas es:", media)