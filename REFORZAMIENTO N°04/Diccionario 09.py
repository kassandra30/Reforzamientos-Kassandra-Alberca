"""Una empresa desea gestionar las facturas pendientes que tiene por pagar,
para esto se creará un diccionario donde tendrá por key el número de factura
“00054” y su value será el coste de la factura. El programa tendrá la opción
de pedir nueva factura (por consola) que se agregará al diccionario. Cada vez
que el área de contabilidad pague una factura se pedirá el número de factura
que fue cancelada, si existe mostrar un mensaje donde indicará “La factura
ya está cancelada” caso contrario “El número de factura no existe”

Considerar que cada vez que se realice algún pago o ingreso de una nueva
factura se mostrará inmediatamente al diccionario actualizado."""

facturas = {
    "00054": 1500.0,
    "00055": 2000.0
}

while True:
    print("\nMenú:")
    print("1. Agregar nueva factura")
    print("2. Pagar factura")
    print("3. Ver facturas")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        num = input("Número de factura: ")
        monto = float(input("Monto de la factura: "))
        facturas[num] = monto
        print("Factura agregada:", facturas)

    elif opcion == "2":
        num = input("Número de factura a pagar: ")
        if num in facturas:
            del facturas[num]
            print("La factura ya está cancelada ✅")
        else:
            print("El número de factura no existe ❌")
        print("Facturas actuales:", facturas)

    elif opcion == "3":
        print("Facturas pendientes:", facturas)

    elif opcion == "4":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida, intenta otra vez.")