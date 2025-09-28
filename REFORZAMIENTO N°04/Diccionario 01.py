"""Crea correctamente un diccionario con los campos de: nombre, edad, salario
y edad.
Convierte tu diccionario finalmente a una lista y muestra el resultado en la
terminal."""

persona = {"nombre": "Kassandra", "edad": 24, "salario": 1500}

lista_persona = list(persona.values())
print("Lista:", lista_persona)