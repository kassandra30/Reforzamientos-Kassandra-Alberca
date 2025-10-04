"""Desarrolla una clase Agenda que administrará contactos. Dentro de una
lista se debe almacenar un diccionario para cada contacto el nombre, el
teléfono, email y DNI. Deberá tener los siguientes métodos:
Añadir contacto, Mostrar contactos y Buscar contacto (Por DNI)
Estructura de la lista cada vez que vas agregando un contacto:
contactos = [
{‘nombre’: “Luis”, ‘telefono’: “997667945”, ‘email’: “luishh@gmail.com”, ‘dni’:
44234239},
{‘nombre’: “Milagros”, ‘telefono’: “997654687”, ‘email’:
“milagros19c@gmail.com”, ‘dni’: 43423211}
]
Agregar por lo menos 4 personas (instanciándolas) para poder luego realizar
la búsqueda de estas personas en la agenda y saber si existen, en caso
contrario indicar: “ ́Nombre ́ no se encuentra anotado en la agenda”"""

class Agenda:
    def __init__(self):
        # Lista donde se guardarán los contactos como diccionarios
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email, dni):
        contacto = {
            'nombre': nombre,
            'telefono': telefono,
            'email': email,
            'dni': dni
        }
        self.contactos.append(contacto)
        print(f"✅ Contacto {nombre} agregado correctamente.\n")

    def mostrar_contactos(self):
        print("📒 Lista de contactos registrados:")
        for c in self.contactos:
            print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}, DNI: {c['dni']}")
        print("\n")

    def buscar_contacto(self, dni):
        for c in self.contactos:
            if c['dni'] == dni:
                print(f"🔎 Contacto encontrado:")
                print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}, DNI: {c['dni']}\n")
                return
        print(f"⚠️ El contacto con DNI {dni} no se encuentra anotado en la agenda.\n")

agenda = Agenda()

agenda.añadir_contacto("Luis", "997667945", "luishh@gmail.com", 44234239)
agenda.añadir_contacto("Milagros", "997654687", "milagros19c@gmail.com", 43423211)
agenda.añadir_contacto("Carlos", "988776655", "carlos2020@gmail.com", 46299887)
agenda.añadir_contacto("Kassandra", "999888777", "kass@gmail.com", 47890123)

agenda.mostrar_contactos()

agenda.buscar_contacto(43423211)   # Existe (Milagros)
agenda.buscar_contacto(12345678)   # No existe