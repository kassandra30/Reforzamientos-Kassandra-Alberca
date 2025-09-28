"""Pedir al usuario que ingrese un nombre y apellidos el cual será usada
por un parámetro para una función que se creará e indicará cuantas letras
tiene el nombre solamente. Usar la función un mínimo de dos veces para dos
personas e indicar quien tiene el nombre con mayor número de caracteres
(condicional)"""

def contar_letras(nombre):
    return len(nombre)   # len() cuenta los caracteres

persona1 = input("Ingresa nombre y apellido de la primera persona: ")
persona2 = input("Ingresa nombre y apellido de la segunda persona: ")

nombre1 = persona1.split()[0]
nombre2 = persona2.split()[0]

letras1 = contar_letras(nombre1)
letras2 = contar_letras(nombre2)

print(f"{nombre1} tiene {letras1} letras")
print(f"{nombre2} tiene {letras2} letras")

if letras1 > letras2:
    print(f"{nombre1} tiene más letras")
elif letras2 > letras1:
    print(f"{nombre2} tiene más letras")
else:
    print("Ambos nombres tienen la misma cantidad de letras")