"""Agrega un nuevo key llamado “dni” con su respectivo valor y luego mostrar
el valor del salario y DNI en consola. También elimina el key edad de tu
diccionario, incluyendo su valor. Mostrar finalmente el diccionario
actualizado."""

persona = {"nombre": "Kassandra", "edad": 24, "salario": 1500}

# Agregar un nuevo key: dni
persona["dni"] = "12345678"

# Mostrar salario y DNI
print("Salario:", persona["salario"])
print("DNI:", persona["dni"])

# Eliminar el key 'edad'
del persona["edad"]

# Mostrar diccionario actualizado
print("Diccionario actualizado:", persona)