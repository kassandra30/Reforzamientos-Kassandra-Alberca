"""Crear una clase Alumno que tenga como atributos el nombre, edad y la
nota final del alumno. Crear los métodos para inicializar sus atributos, otro
para imprimirlos y un metodo para mostrar un mensaje con el resultado de la
nota, si ha aprobado (mayor o igual a 13) o no el alumno. Instanciar la clase
por lo menos 4 veces (4 alumnos)"""

class Alumno:
    def __init__(self, nombre, edad, nota_final):
        self.nombre = nombre
        self.edad = edad
        self.nota_final = nota_final

    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Nota final: {self.nota_final}")

    def resultado(self):
        if self.nota_final >= 13:
            print(f"{self.nombre} ha aprobado ✅")
        else:
            print(f"{self.nombre} no ha aprobado ❌")


# ---- Instanciamos 4 alumnos ----
alumno1 = Alumno("Ana", 18, 15)
alumno2 = Alumno("Luis", 19, 12)
alumno3 = Alumno("María", 20, 17)
alumno4 = Alumno("Pedro", 18, 10)

# Mostramos los datos y resultados
for alumno in [alumno1, alumno2, alumno3, alumno4]:
    alumno.mostrar_datos()
    alumno.resultado()
    print()