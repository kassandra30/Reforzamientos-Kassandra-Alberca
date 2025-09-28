"""Crea una función que al ingresar dos números por parámetro mostrará
todos los cuadrados de los números que hay entre ellos (Usar la función una
vez y mostrar el resultado por consola). Los números serán ingresados y
solicitados al usuario."""

def mostrar_cuadrados(a, b):
    for i in range(a, b+1):
        print(i, "→", i**2)

x = int(input("Número inicial: "))
y = int(input("Número final: "))

mostrar_cuadrados(x, y)