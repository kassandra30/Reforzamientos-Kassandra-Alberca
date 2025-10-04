"""Crear una clase llamada Soldado para un juego sobre un mapa la cual
deberá tener como atributos en el constructor posición X y posición Y las
cuales iniciarán en 0, agregar un nombre a este soldado dentro de estos
atributos.
La clase debe tener los siguientes métodos. Caminar hacia el eje X en donde
se indicará cuántos pasos dará y otra clase que le permitirá caminar por el
eje Y, en caso se indique un número negativo indicar que solo puede llegar
hasta el 0 si es menor a los pasos ya dados.
Crear finalmente un metodo adicional que irá guardando los pasos que ha dado
dentro de una lista para que finalmente al usar este metodo me muestre el
historial de movimientos del Soldado, tanto en el eje X y en eje Y
Instanciar un mínimo de 5 movimientos para que muestre finalmente el
historial de pasos de tu soldado"""

class Soldado:
    def __init__(self, nombre):
        self.nombre = nombre
        self.x = 0
        self.y = 0
        self.historial = []  # guarda los movimientos

    def mover_x(self, pasos):
        if self.x + pasos < 0:
            self.x = 0
        else:
            self.x += pasos
        self.historial.append(f"Movió en X a {self.x}")

    def mover_y(self, pasos):
        if self.y + pasos < 0:
            self.y = 0
        else:
            self.y += pasos
        self.historial.append(f"Movió en Y a {self.y}")

    def mostrar_historial(self):
        print(f"\nHistorial de movimientos de {self.nombre}:")
        for mov in self.historial:
            print(mov)
        print(f"Posición final -> X: {self.x}, Y: {self.y}")

soldado1 = Soldado("Rambo")

soldado1.mover_x(5)
soldado1.mover_y(3)
soldado1.mover_x(-2)
soldado1.mover_y(4)
soldado1.mover_x(1)

soldado1.mostrar_historial()