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
    

class Lista_funciones:
    def __init__(self):
        self.listarFunciones = []
        self.cargar_datos()

    def cargar_datos(self):
        datos = [
            Medicamento(1, "Paracetamol", 2.50, 30),
            Medicamento(2, "Ibuprofeno", 3.20, 20),
        ]
        for medicamento in datos:
            self.listarFunciones.append(medicamento)
            print(f"Datos cargados correctamente: {medicamento}")

    def registrar_funcion(self, nombre, precio, cajas):
        codigo = len(self.listarFunciones) + 1
        medicamento = Medicamento(codigo, nombre, precio, cajas)
        self.listarFunciones.append(medicamento)
        return medicamento

    def mostrar(self):
        print("Código  |   Nombre   |  Precio   |  Cajas")
        for elemento in self.listarFunciones:
            print(elemento)

    def buscar_por_codigo(self, codigo):
        for elemento in self.listarFunciones:
            if elemento.codigo == codigo:
                return elemento
        return None

    def vender_medicamentos(self, codigo, cantidad):
        medicamento = self.buscar_por_codigo(codigo)
        if medicamento is None:
            print("Error: no existe ese código.")
            return False
        return medicamento.vender(cantidad)
