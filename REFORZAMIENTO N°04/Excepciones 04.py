"""Crear una función saluda_fecha(nombre, dia, mes, anio) que contendrá una
excepción para el siguiente bloque de código y tu programa no se bloquee.
Además, imprime un mensaje al usuario la causa y/o solución (Pedir
nombre, día, mes, año por consola):
Nombre: No debe recibir un dato numérico, sino decírselo al usuario Día, mes
y año: No debe recibir un dato string, sino decírselo al usuario

cadena = "Hello NOMBRE, hoy estamos DÍA de MES del AÑO"
# Hello Leonardo, hoy estamos 04 de agosto del 2025

Independientemente del resultado, debe imprimir “Operación
finalizada” al final
- Usar try, except, finally
Usar la función al menos 3 veces, incluyendo casos de error"""

def saluda_fecha(nombre, dia, mes, anio):
    try:
        if nombre.isdigit():
            raise ValueError("El nombre no puede ser numérico")
        dia, anio = int(dia), int(anio)
        if not isinstance(mes, str):
            raise TypeError("El mes debe ser un texto")

        print(f"Hello {nombre}, hoy estamos {dia:02d} de {mes} del {anio}")
    except Exception as e:
        print("Error:", e)
    finally:
        print("Operación finalizada\n")


# ---- Probando 3 veces ----
print("Caso 1: válido")
saluda_fecha("Kassandra", 27, "setiembre", 2025)

print("Caso 2: nombre numérico")
saluda_fecha("1234", 20, "agosto", 2024)

print("Caso 3: día no numérico")
saluda_fecha("Nicol", "quince", "abril", "dos mil")