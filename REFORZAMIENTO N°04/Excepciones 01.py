"""Crear una función llamada division_segura(a, b) que recibirá dos
números e intentará devolver la división de a entre b
Si b es cero, debe capturar la excepción y mostrar mensaje “Error: no puedes
dividir entre cero”
Si ambos valores son válidos deben imprimir el resultado Independientemente
del resultado, debe imprimir “Operación finalizada” al final
- Usar try, except, finally

- Valida que los datos ingresados sean numéricos de lo contrario mostrar
“Error: Entrada no numérica”
- Usarás la función al menos 3 veces incluyendo un caso de error"""

def division_segura(a, b):
    try:
        a, b = float(a), float(b)
        print("Resultado:", a / b)
    except ValueError:
        print("Error: Entrada no numérica")
    except ZeroDivisionError:
        print("Error: no puedes dividir entre cero")
    finally:
        print("Operación finalizada\n")

print("Caso 1: válido")
division_segura(28, 2)

print("Caso 2: división entre cero")
division_segura(12, 0)

print("Caso 3: entrada no numérica")
division_segura("hola", 5)
