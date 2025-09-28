"""Crear un diccionario con 6 departamentos del país.
- Borrar cualquier departamento, usando la palabra reservada del.
- Actualizar el penúltimo departamento por otro.

- Comprobar que no existe este departamento borrado dentro del
diccionario."""

departamentos = {
    1: "Lima",
    2: "Cusco",
    3: "Arequipa",
    4: "Piura",
    5: "La Libertad",
    6: "Junín"
}

print("Diccionario inicial:", departamentos)

del departamentos[2]
print("Después de borrar Cusco:", departamentos)

departamentos[5] = "Ayacucho"
print("Después de actualizar penúltimo:", departamentos)

if "Cusco" not in departamentos.values():
    print("Cusco ya no está en el diccionario ✅")
else:
    print("Cusco aún existe en el diccionario ❌")