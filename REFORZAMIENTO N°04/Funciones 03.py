"""Crear una función que sume los dígitos del número ingresado y muestre
por consola la suma de todos estos dígitos."""

def suma_digitos(num):
    return sum(int(d) for d in str(num))

n = int(input("Ingrese un número: "))
print("La suma de sus dígitos es:", suma_digitos(n))