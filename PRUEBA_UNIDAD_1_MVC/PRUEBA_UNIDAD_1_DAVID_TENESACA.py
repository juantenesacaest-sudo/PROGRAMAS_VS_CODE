
"""
==================================================================
CASO 6 FARMACIA SAN JOSE
==================================================================
"""

class Medicamento:
    def __init__(self, codigo, nombre, precio, cajas):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.cajas = cajas

    def vender(self, cantidad):
        if cantidad <= 0:
            print("Error: la cantidad debe ser mayor que cero.")
            return False
        if cantidad > self.cajas:
            print(f"Error: solo hay {self.cajas} cajas.")
            return False
        self.cajas -= cantidad
        return True

    def __str__(self):
        return f"{self.codigo}|{self.nombre}|{self.precio}|{self.cajas}"


def buscar(lista):
    print("Código | Nombre | Precio | Cajas")
    for elemento in lista:
        print(elemento)


def buscar_por_codigo(lista, codigo):
    for elemento in lista:
        if elemento.codigo == codigo:
            return elemento
    return None


def agregar_medicamento(lista):
    nombre = input("Nombre: ")
    precio = float(input("Precio: ").replace(",", "."))
    cajas = int(input("Cajas: "))
    codigo = len(lista) + 1
    lista.append(Medicamento(codigo, nombre, precio, cajas))
    print(f"Registrado con el código {codigo}.")


lista = [
    Medicamento(1, "Paracetamol", 2.50, 30),
    Medicamento(2, "Ibuprofeno", 3.20, 20),
]

while True:
    print()
    print("MENÚ")
    print("1. Registrar medicamento")
    print("2. Mostrar medicamentos")
    print("3. Vender medicamento")
    print("4. Salir")
    opcion = input("Seleccione una opción: ").strip()

    if opcion == "1":
        agregar_medicamento(lista)
    elif opcion == "2":
        buscar(lista)
    elif opcion == "3":
        codigo = int(input("Código: "))
        elemento = buscar_por_codigo(lista, codigo)
        if elemento is None:
            print("Error: no existe ese código.")
        else:
            cantidad = int(input("Cantidad: "))
            if elemento.vender(cantidad):
                print(f"Listo. Quedan {elemento.cajas} cajas.")
    elif opcion == "4":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")