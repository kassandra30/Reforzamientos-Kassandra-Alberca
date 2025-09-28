"""Ingresar el nombre de tu carrera dentro de los valores que tienes en tu
diccionario.
- Mostrar en consola los valores de tu carrera y nombre agregándolos a
una variable c/u"""

persona = {
    "nombre": "Kassandra",
    "edad": 24,
    "salario": 1500
}

persona["carrera"] = "Ingeniería Química"

mi_nombre = persona["nombre"]
mi_carrera = persona["carrera"]

print("Nombre:", mi_nombre)
print("Carrera:", mi_carrera)