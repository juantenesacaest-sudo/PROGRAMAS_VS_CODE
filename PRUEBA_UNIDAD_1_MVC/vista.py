

class VistaOperacion:

    def menu(self):
        print("\n ----- FARMACIA SAN JOSE -------")
        print("MENÚ")
        print("1. Registrar medicamento")
        print("2. Mostrar medicamentos")
        print("3. Vender medicamento")
        print("4. Salir")
        opcion=self.leer_mensaje("Ingrese la opcion: ")
        return opcion

    def agregar_medicamento(self):
        nombre = self.leer_mensaje("Ingrese el nombre: ")
        precio = self.leer_decimal("Ingrese el precio: ")
        while precio<=0:
            print("Debe ser un precio valido")
            precio = self.leer_decimal("Ingrese el precio: ")
        cajas = self.leer_entero("Ingrese la cantidad de cajas: ")
        while cajas<=0:
            print("Debe ser un número valido: ")
            cajas = self.leer_entero("Ingrese la cantidad de cajas: ")

        return nombre, precio, cajas

    def vender_medicamento(self):
        codigo=int(self.leer_entero("Ingrese el codigo del medicamento: "))
        cantidad=self.leer_entero("Ingrese la cantidad que va a vender: ")
        while cantidad<=0:
            print("Debe ser un número mayor a 0")
            cantidad=self.leer_entero("Ingrese la cantidad que va a vender: ")
        return codigo, cantidad

    def mostrar_medicamentos(self, medicamentos):
        print(f"Codigo  |    Nombre    |  Precio  |  Cajas")
        for i in medicamentos:
            print(i)


    def leer_entero(self, mensaje):
        while True:
            try:
                return int(input(mensaje).strip())
            except ValueError:
                print("Debe ingresar un número")

    def leer_decimal(self, mensaje):
        while True:
            try:
                return float(input(mensaje).strip().replace(",","."))
            except ValueError:
                print("Debe de ingresar un decimal valido")

    def leer_mensaje(self, mensaje):
        while True:
            texto=input(mensaje).strip()
            if texto=="" or "," in texto:
                print("El mensaje no puede estar vacio y no puede llevar comas")
            else:
                return texto
    def error(self, mensaje):
            print("Mesaje de error")

    def mostrar_mensaje(self, mensaje="Operacion correcta"):
        print(mensaje)
            