"""Crear una función que aceptará por parámetro dos valores que serán
ingresados por el usuario, una lista donde los valores serán llenados por el
usuario también y un segundo parámetro que eliminará de la lista que fue
ingresada a la función, finalmente el output de la función será la lista
actualizada sin el valor que se sacará de la lista. Mostrar también la lista
original y el número que fue eliminado."""

lista = [int(x) for x in input("Ingresa números: ").split()]
num = int(input("Número a eliminar: "))
print("Lista original:", lista)
if num in lista: lista.remove(num)
print("Número eliminado:", num)
print("Lista actualizada:", lista)