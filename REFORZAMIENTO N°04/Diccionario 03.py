"""Convertir tu diccionario a una lista y mostrar en consola el tipo de datos
final que tienes."""

persona = {"nombre": "Kassandra", "edad": 24, "salario": 1500}
print("Diccionario inicial:", persona)


lista_persona = list(persona.items())
print("Diccionario convertido a lista:", lista_persona)



persona["dni"] = "12345678"
print("Salario:", persona["salario"])
print("DNI:", persona["dni"])

del persona["edad"]
print("Diccionario actualizado:", persona)


lista_final = list(persona.items())
print("Diccionario convertido a lista final:", lista_final)
print("Tipo de dato final:", type(lista_final))