"""Haciendo el uso de *args y **kwargs aplicarlo debidamente para
decorar una función que recibirá 6 argumentos los cuales se
multiplicarán entre ellos (3 de ellos serán usado con **kwargs)
Mensaje previo al usar el decorador “Está por ejecutarse la función” y
mensaje luego de usar el decorador “La función ha sido ejecutado
correctamente”
Usar la función decorada al menos 3 veces"""

def mensaje_ejecucion(func):
    def wrapper(*args, **kwargs):
        print("Está por ejecutarse la función...")
        resultado = func(*args, **kwargs)
        print("La función ha sido ejecutada correctamente.\n")
        return resultado
    return wrapper

@mensaje_ejecucion
def multiplicar_numeros(a, b, c, **kwargs):
    x = kwargs.get('x')
    y = kwargs.get('y')
    z = kwargs.get('z')
    resultado = a * b * c * x * y * z
    print(f"El resultado de la multiplicación es: {resultado}")
    return resultado

multiplicar_numeros(1, 2, 3, x=4, y=5, z=6)
multiplicar_numeros(2, 3, 4, x=1, y=2, z=3)
multiplicar_numeros(5, 2, 1, x=2, y=3, z=4)
