"""3. Crear un decorador conteo_parametros(funcion) donde imprimirá la
cantidad de argumentos que tiene la función a decorar usando *args y
**kwargs.
Mensaje previo “La cantidad de argumentos que tiene la función es”
mensaje post “La función decoradora terminó de ejecutarse
correctamente”
Ejemplo: Al usar una función suma que creamos:
suma(4, 1, 10, 2, 50, 64)
Salida:
“La cantidad de argumentos que tiene la función es 5”
“La función decoradora terminó de ejecutarse correctamente”
Consideración:
Todos los parámetros ingresados deben ser enteros, caso sean String
alguno de ellos indicar al usuario: “Solo está admitido datos enteros,
no se podrá realizar la suma”
Usar la función al menos 3 veces"""


def conteo_parametros(func):
    def wrapper(*args, **kwargs):

        for arg in args:
            if not isinstance(arg, int):
                print("Solo está admitido datos enteros, no se podrá realizar la suma.\n")
                return
        for valor in kwargs.values():
            if not isinstance(valor, int):
                print("Solo está admitido datos enteros, no se podrá realizar la suma.\n")
                return

        total_args = len(args) + len(kwargs)
        print(f"La cantidad de argumentos que tiene la función es {total_args}")

        resultado = func(*args, **kwargs)

        print("La función decoradora terminó de ejecutarse correctamente.\n")
        return resultado

    return wrapper

@conteo_parametros
def suma(*args, **kwargs):
    total = sum(args) + sum(kwargs.values())
    print(f"La suma total es: {total}")
    return total

suma(4, 1, 10, 2, 50, 64)
suma(3, 7, x=10, y=20)
suma(5, "hola", 7)